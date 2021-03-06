import os
import sys
import time
import traceback
from datetime import date

import matplotlib
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from PyQt5.QtCore import QTimer, QCoreApplication
from PyQt5.QtWidgets import QDialog, QApplication, QGraphicsScene, QMessageBox
from PyQt5.QtGui import QIntValidator
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import MicroScanReader
import OmronFinsTcp
import login
import plc_setting
import result_generator
import ui_main

matplotlib.use("Qt5Agg")  # 声明使用QT5


class PressureChart(FigureCanvasQTAgg):
    def __init__(self, size, parent=None, dpi=100):
        self.figure = Figure(figsize=size, dpi=dpi)
        FigureCanvasQTAgg.__init__(self, self.figure)
        self.setParent(parent)
        '''
        调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法
        '''
        self.axes = self.figure.add_subplot(111)
        self.axes.set_autoscaley_on(True)
        self.axes.set_ylabel("Pressure(Kpa)")
        self.axes.set_xlabel("Time(second)")
        self.axes.set_xlim([0, 15.0])
        self.axes.set_ylim([0, 70])
        self.axes.grid(True, linestyle='-.')
        xmajorLocator = MultipleLocator(1.0)
        self.axes.xaxis.set_major_locator(xmajorLocator)
        ymajorLocator = MultipleLocator(5)
        self.axes.yaxis.set_major_locator(ymajorLocator)
        self.line, = self.axes.plot([], [])
        self.line.set_linewidth(0.5)

    def draw_threshold(self, low, high):
        try:
            self.thres_low.set_ydata(low)
        except:
            self.thres_low = self.axes.axhline(y=low, linewidth=0.5, color='blue')
        try:
            self.thres_high.set_ydata(high)
        except:
            self.thres_high = self.axes.axhline(y=high, linewidth=0.5, color='blue')
        # self.axes.plot()
        self.figure.canvas.draw()
        # self.figure.canvas.flush_events()

    def draw_pressure(self, x, y):
        self.line.set_xdata(x)
        self.line.set_ydata(y)
        # self.axes.relim()
        # self.axes.autoscale_view()
        # self.axes.plot()
        self.figure.canvas.draw()
        # self.figure.canvas.flush_events()

class TimerMessageBox(QMessageBox):
    def __init__(self, timeout=3, parent=None):
        super(TimerMessageBox, self).__init__(parent)
        self.setWindowTitle("wait")
        self.time_to_wait = timeout
        self.setText("{0} 秒后重新连接PLC".format(timeout))
        self.setStandardButtons(QMessageBox.NoButton)
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.changeContent)
        self.timer.start()

    def changeContent(self):
        self.setText("{0} 秒后重新连接PLC".format(self.time_to_wait))
        self.time_to_wait -= 1
        if self.time_to_wait <= 0:
            self.close()

    def closeEvent(self, event):
        self.timer.stop()
        event.accept()

warnings_dict = {0: '硅胶使用寿命已到，请及时更换!\n',
                 1: '热保护跳闸，请手动复位\n',
                 2: '急停中\n',
                 3: '光栅异常\n',
                 4: '没有读到条码\n',
                 5: '重新开始请复位\n',
                 7: '抽气超时\n'
                 }

manual_dict = {0: '真空泵手动中\n',
               1: '下压缸手动中\n',
               2: '阀1（快速阀）手动中\n',
               3: '阀2（慢速阀）手动中\n',
               4: '阀3（排气阀）手动中\n',
               5: 'OK手动中\n',
               6: 'NG手动中\n',
               7: '蜂鸣器手动中\n',
               12: '复位按钮\n',
               13: '准备就绪（扫描枪&软件）\n',
               14: '生产计数清零\n'
               }

warnings_to_reset = [1, 2, 7]

STATE_TO_CONNECT = 1
STATE_TO_START = 2
STATE_TO_READ = 3
STATE_TO_KEEP = 4
STATE_TO_STOP = 5
STATE_TO_RESET = 6

class PressureUI(QDialog):
    def __init__(self):
        super(PressureUI, self).__init__()
        self.plc = OmronFinsTcp.OmronPLC()
        self.plc.signal.connect(self.plc_connect_failed)
        self.scanner = MicroScanReader.MicroScanReader()
        self.date = date.today().strftime('%Y-%b-%d')
        if not os.path.exists('结果/'):
            os.makedirs('结果/')
        self.result_file = result_generator.PLCResult('结果/' + self.date + '.xlsx')
        self.result = {}
        self.timestamp = []
        self.pressure = []
        self.max_pressure = 0
        self.bar_code = ''
        self.plc_open = False
        self.scanner_open = False
        self.state = STATE_TO_CONNECT
        '''
        setup Qt UI
        '''
        self.ui = ui_main.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle(QCoreApplication.translate("Dialog", "气密量测系统"))
        self.ui.tabs.currentChanged.connect(self.tab_changed)
        self.io_table_in_label_list = [self.ui.io_table_in_label_0,
                                       self.ui.io_table_in_label_1,
                                       self.ui.io_table_in_label_2,
                                       self.ui.io_table_in_label_3,
                                       self.ui.io_table_in_label_4,
                                       self.ui.io_table_in_label_5,
                                       self.ui.io_table_in_label_6,
                                       self.ui.io_table_in_label_7]
        self.io_table_out_label_list = [self.ui.io_table_out_label_0,
                                        self.ui.io_table_out_label_1,
                                        self.ui.io_table_out_label_2,
                                        self.ui.io_table_out_label_3,
                                        self.ui.io_table_out_label_4,
                                        self.ui.io_table_out_label_5,
                                        self.ui.io_table_out_label_6,
                                        self.ui.io_table_out_label_7]
        self.variable_label_list = [self.ui.variable_label_0, self.ui.variable_label_1]
        self.variable_address_list = []
        if (os.path.isfile('lable_name.txt')):
            with open('lable_name.txt', 'r', encoding="utf8") as f:
                for i, name in enumerate(f):
                    self.variable_label_list[i].setText(name)
        self.silicate_count_total_validator = QIntValidator(0, 30000, self)
        self.ui.silicate_count_total_edit.setValidator(self.silicate_count_total_validator)
        self.setting = self.load_plc_setting()
        self.apply_plc_setting_to_ui(self.setting)
        '''
        register button click event
        '''
        self.ui.reset_button.clicked.connect(self.reset_clicked)
        self.ui.auto_button.clicked.connect(self.auto_clicked)
        self.ui.stop_button.clicked.connect(self.stop_clicked)
        self.ui.save_setting_button.clicked.connect(self.save_setting_clicked)
        self.ui.save_setting_button_2.clicked.connect(self.save_setting_clicked)
        self.ui.total_count_clear_button.clicked.connect(self.total_count_clear_clicked)
        self.ui.silicate_count_current_clear_button.clicked.connect(self.silicate_count_current_clear_clicked)
        self.ui.scanner_enable_checkbox.clicked.connect(self.scanner_connect)
        self.ui.io_table_out_button_0.clicked.connect(self.io_table_out_0_clicked)
        self.ui.io_table_out_button_1.clicked.connect(self.io_table_out_1_clicked)
        self.ui.io_table_out_button_2.clicked.connect(self.io_table_out_2_clicked)
        self.ui.io_table_out_button_3.clicked.connect(self.io_table_out_3_clicked)
        self.ui.io_table_out_button_4.clicked.connect(self.io_table_out_4_clicked)
        self.ui.io_table_out_button_5.clicked.connect(self.io_table_out_5_clicked)
        self.ui.io_table_out_button_6.clicked.connect(self.io_table_out_6_clicked)
        self.ui.io_table_out_button_7.clicked.connect(self.io_table_out_7_clicked)
        '''
        init pressure chart
        '''
        self.graphic_scene = QGraphicsScene()
        self.ui.pressure_view.setScene(self.graphic_scene)
        # FIXME: figure size should be handled better
        figure_size = (self.ui.pressure_view.width() / 110, self.ui.pressure_view.height() / 110)
        self.chart = PressureChart(figure_size)
        self.graphic_scene.addWidget(self.chart)
        self.update_pressure_threshold()
        '''
        set up timer to check device status single shot
        '''
        QTimer.singleShot(1000, self.connect_clicked)
        '''
        set up timer to check device status periodically
        '''
        self.dev_status_interval = 1000
        self.dev_status_timer = QTimer()
        self.dev_status_timer.setSingleShot(False)
        self.dev_status_timer.setInterval(self.dev_status_interval)
        self.dev_status_timer.timeout.connect(self.dev_status_timeout)
        '''
        set up timer to check pressure periodically
        '''
        self.pressure_interval = 1
        self.fsm_timer = QTimer()
        self.fsm_timer.setSingleShot(False)
        self.fsm_timer.setInterval(self.pressure_interval)
        self.fsm_timer.timeout.connect(self.fsm_timeout)
        '''
        set up timer to check io table periodically
        '''
        self.io_table_interval = 200
        self.io_table_timer = QTimer()
        self.io_table_timer.setSingleShot(False)
        self.io_table_timer.setInterval(self.io_table_interval)
        self.io_table_timer.timeout.connect(self.io_table_timeout)
        '''
        set up debug timer periodically
        '''
        self.debug_interval = 200
        self.debug_timer = QTimer()
        self.debug_timer.setSingleShot(False)
        self.debug_timer.setInterval(self.debug_interval)
        self.debug_timer.timeout.connect(self.debug_timeout)
        '''
        bar code receive setup
        '''
        self.bc_receive = None

    def scanner_connect(self):
        if self.ui.scanner_enable_checkbox.isChecked():
            scanner_ip = self.ui.code_scannner_ip_edit.text()
            scanner_port = int(self.ui.code_scanner_port_edit.text())
            if not self.scanner.open(scanner_ip, scanner_port):
                self.ui.connection_label.setText('扫码枪连接失败')
                self.ui.connection_label.setStyleSheet("font-size:24pt; font-weight:600; color:#ff0000")
            else:
                self.ui.connection_label.setText("连接正常")
                self.ui.connection_label.setStyleSheet("font-size:24pt; font-weight:600; color:#00ff00")
        else:
            self.scanner.close()

    def plc_connect(self):
        plc_ip = self.ui.plc_ip_edit.text()
        plc_port = int(self.ui.plc_port_edit.text())
        self.plc = OmronFinsTcp.OmronPLC()
        self.plc.signal.connect(self.plc_connect_failed)
        if self.plc.openFins(plc_ip, plc_port):
            self.ui.connection_label.setText("连接正常")
            self.ui.connection_label.setStyleSheet("font-size:24pt; font-weight:600; color:#00ff00")
            self.fsm_timer.start()
            self.dev_status_timer.start()
        else:
            error_text = 'PLC重连失败,重连中'
            self.ui.connection_label.setText(error_text)
            self.ui.connection_label.setStyleSheet("font-size:24pt; font-weight:600; color:#ff0000")
            QTimer.singleShot(5000, self.plc_connect)

    # TODO handle PLC and scanner lost at runtime
    def dev_status_timeout(self):
        try:
            warnings = self.plc.read('C181')
            manual = self.plc.read('C183')
            total_count = self.plc.read('D500')
            self.ui.total_count_lcd.display(total_count)
            silicate_count_current = self.plc.read('D504')
            self.ui.silicate_count_current_lcd.display(silicate_count_current)
            if warnings & 1 << 8:
                self.ui.auto_button.setStyleSheet("font-size:16pt; background-color: green")
            else:
                self.ui.auto_button.setStyleSheet('font-size:16pt')
            text = ''
            for bit in warnings_dict:
                if (warnings & 1 << bit):
                    text += warnings_dict[bit]
            for bit in manual_dict:
                if (manual & 1 << bit):
                    text += manual_dict[bit]
            self.ui.dev_info_browser.setText(text)
            self.ui.dev_info_browser.setStyleSheet("font-size:12pt; font-weight:600; color:#ff0000")
            if warnings & (1 << 1 | 1 << 2 | 1 << 7):
                self.state = STATE_TO_RESET
        except Exception as e:
            print('dev_status_timeout: ', repr(e))
            traceback.print_exc()

    def pressure_timeout(self):
        # start read pulse
        try:
            if len(self.timestamp) > 0:
                self.timestamp.append(time.time() - self.pressure_start_time)
            else:
                self.pressure_start_time = time.time()
                self.timestamp.append(0)
            value = self.plc.read('D524')
            if value >= 65000:
                value = 0
            value = value / 100.0
            self.pressure.append(value)
            self.ui.current_pressure_lcd.display(value)
            if value > self.max_pressure:
                self.max_pressure = value
            self.chart.draw_pressure(self.timestamp, self.pressure)

            if self.plc.test('C181', 6):
                self.state = STATE_TO_STOP
                self.pressure_keep_time = time.time()
        except Exception as e:
            print('pressure_timeout: ', repr(e))
            traceback.print_exc()

    def pressure_timeout_2(self):
        try:
            if not self.plc.test('C184', 0):
                pressure_var = self.plc.read('D526') / 100.0
                print(pressure_var)
                if pressure_var > 650:
                    pressure_var = 0
                pressure_var_sign = self.plc.read('D528')
                if pressure_var_sign == 1:
                    pressure_var = -pressure_var
                self.ui.max_pressure_lcd.display(pressure_var)
                io_table_out = self.plc.read('C100')
                if io_table_out & 1 << 5:
                    test_result = 'OK'
                    self.ui.status_label.setText('OK')
                    self.ui.status_label.setStyleSheet("font-size:48pt; font-weight:600; color:green")
                elif io_table_out & 1 << 6:
                    test_result = 'NG'
                    self.ui.status_label.setText('NG')
                    self.ui.status_label.setStyleSheet("font-size:48pt; font-weight:600; color:red")
                else:
                    test_result = 'NG'
                    self.ui.status_label.setText('NG')
                    self.ui.status_label.setStyleSheet("font-size:48pt; font-weight:600; color:red")
                if not self.plc.test('C181', 7):
                    self.result_file.add_result(format(time.time() - self.pressure_start_time, '.1f'), pressure_var,
                                                test_result, self.bar_code)
                self.state = STATE_TO_START
                return
            if time.time() - self.pressure_keep_time >= self.setting['pressure_hold_time'] - 0.5:
                return
            if len(self.timestamp) > 0:
                self.timestamp.append(time.time() - self.pressure_start_time)
            else:
                self.pressure_start_time = time.time()
                self.timestamp.append(0)
            value = self.plc.read('D524')
            if value >= 65000:
                value = 0
            value = value / 100.0
            self.pressure.append(value)
            self.ui.current_pressure_lcd.display(value)
            if value > self.max_pressure:
                self.max_pressure = value
            self.chart.draw_pressure(self.timestamp, self.pressure)
            # self.graphic_scene.addWidget(self.chart)
            # self.ui.pressure_view.show()
        except Exception as e:
            print('pressure_timeout: ', repr(e))
            traceback.print_exc()

    def pressure_read_check(self):
        if self.plc.test('C184', 0):
            self.state = STATE_TO_KEEP

    def fsm_timeout(self):
        if self.state == STATE_TO_START:
            self.start_check()
        elif self.state == STATE_TO_READ:
            self.pressure_read_check()
        elif self.state == STATE_TO_KEEP:
            self.pressure_timeout()
        elif self.state == STATE_TO_STOP:
            self.pressure_timeout_2()
        elif self.state == STATE_TO_RESET:
            self.reset_w80()

    def reset_w80(self):
        try:
            self.plc.clear('W80', 0)
            self.plc.clear('W80', 1)
        except Exception as e:
            print('reset_w80: ', repr(e))
            traceback.print_exc()
        self.state = STATE_TO_START

    def debug_timeout(self):
        d524 = self.plc.read('D524')
        if d524 > 65000:
            d524 = 0
        self.ui.d524_lcd.display(d524 / 100.0)
        warning = self.plc.read('C181')
        if warning & 1 << 6:
            self.ui.d538_lcd.display(self.plc.read('D538') / 100.0)
        self.ui.d540_lcd.display(self.plc.read('D540') / 100.0)

    def start_check(self):
        try:
            warning = self.plc.read('C181')
            if warning & 1 << 9:
                print('Button pushed')
                self.timestamp = []
                self.pressure = []
                self.bar_code = ''
                self.ui.status_label.setText('')
                self.ui.dev_bar_code_browser.setText('')
                self.ui.max_pressure_lcd.display(0)
                if self.ui.scanner_enable_checkbox.isChecked():
                    self.bar_code = self.scanner.read()
                    print('read bar code: ', self.bar_code)
                    if self.bar_code:
                        self.ui.dev_bar_code_browser.setText(self.bar_code)
                        print('write C180 to start')
                        self.plc.set('C180', 13)
                        self.state = STATE_TO_READ
                    else:
                        print('read bar code failed')
                else:
                    self.bar_code = ''
                    self.ui.dev_bar_code_browser.setText(self.bar_code)
                    print('write C180 to start without bar code')
                    self.plc.set('C180', 13)
                    self.state = STATE_TO_READ
        except Exception as e:
            print('start_check: ', repr(e))
            traceback.print_exc()

    def io_table_timeout(self):
        try:
            io_table_in = self.plc.read('C0')
            io_table_out = self.plc.read('C100')
            for label in self.io_table_in_label_list:
                if io_table_in & (1 << self.io_table_in_label_list.index(label)):
                    label.setStyleSheet("QLabel {background-color: green}")
                else:
                    label.setStyleSheet("QLabel {background-color: red}")
            for label in self.io_table_out_label_list:
                if io_table_out & (1 << self.io_table_out_label_list.index(label)):
                    label.setStyleSheet("QLabel {background-color: green}")
                else:
                    label.setStyleSheet("QLabel {background-color: red}")
        except Exception as e:
            print('io_table_timeout: ', repr(e))
            traceback.print_exc()

    def connect_clicked(self):
        plc_ip = self.ui.plc_ip_edit.text()
        plc_port = int(self.ui.plc_port_edit.text())
        scanner_ip = self.ui.code_scannner_ip_edit.text()
        scanner_port = int(self.ui.code_scanner_port_edit.text())
        self.plc_open = self.plc.openFins(plc_ip, plc_port)
        if self.ui.scanner_enable_checkbox.isChecked():
            self.scanner_open = self.scanner.open(scanner_ip, scanner_port)
        else:
            self.scanner_open = True
        if self.plc_open and self.scanner_open:
            # TODO how to use status label
            self.ui.connection_label.setText("连接正常")
            self.ui.connection_label.setStyleSheet("font-size:24pt; font-weight:600; color:#00ff00")
            self.fsm_timer.start()
            self.dev_status_timer.start()
            self.apply_plc_setting_to_plc(self.setting)
            self.state = STATE_TO_START
        else:
            error_text = ''
            if not self.plc_open:
                error_text += 'PLC '
            if not self.scanner_open:
                error_text += '扫码枪 '
            error_text += '断开,重连中...'
            self.ui.connection_label.setText(error_text)
            self.ui.connection_label.setStyleSheet("font-size:24pt; font-weight:600; color:#ff0000")
            QTimer.singleShot(5000, self.connect_clicked)

    def plc_connect_failed(self):
        try:
            error_text = 'PLC断开,重连中'
            self.ui.connection_label.setText(error_text)
            self.ui.connection_label.setStyleSheet("font-size:24pt; font-weight:600; color:#ff0000")
            self.fsm_timer.stop()
            self.dev_status_timer.stop()
            self.io_table_timer.stop()
            self.debug_timer.stop()
            self.plc.close()
        except:
            pass
        QTimer.singleShot(5000, self.connect_clicked)

    def load_plc_setting(self):
        plcsetting = plc_setting.PLCSetting()
        setting = self.get_setting_from_ui()
        setting_file = plcsetting.read('plcsetting.csv')
        for s in setting_file:
            setting[s] = setting_file[s]
        setting1 = {}
        for key in setting:
            setting1[key] = float(setting[key])
        return setting1

    def get_setting_from_ui(self):
        setting = {}
        # setting['pressure_coef'] = float(self.ui.pressure_coef_edit.text())
        setting['pressure_var'] = float(self.ui.pressure_var_edit.text())
        setting['pumping_time'] = float(self.ui.pumping_time_edit.text())
        setting['pressure_hold_time'] = float(self.ui.pressure_hold_time_edit.text())
        setting['pressure_thres_low'] = float(self.ui.pressure_thres_low_edit.text())
        setting['pressure_thres_high'] = float(self.ui.pressure_thres_high_edit.text())
        setting['pressure_approx'] = float(self.ui.pressure_approx_edit.text())
        setting['pressure_target'] = float(self.ui.pressure_target_edit.text())
        setting['silicate_count_total'] = float(self.ui.silicate_count_total_edit.text())
        if setting['silicate_count_total'] > 30000:
            setting['silicate_count_total'] = 30000.0
            self.ui.silicate_count_total_edit.setText(str(int(setting['silicate_count_total'])))
        setting['pump_stop_timeout'] = float(self.ui.pump_stop_timeout_edit.text())
        setting['reserve1'] = float(self.ui.variable_edit_0.text())
        setting['reserve2'] = float(self.ui.variable_edit_1.text())
        return setting

    def save_plc_setting(self, setting):
        plcsetting = plc_setting.PLCSetting()
        plcsetting.save('plcsetting.csv', setting)

    def apply_plc_setting_to_plc(self, setting):
        # TODO check update UI when loading csv file
        # self.plc.write('D508', int(setting['pressure_coef'] * 100))
        self.plc.write('D510', int(setting['pressure_var'] * 100))
        self.plc.write('D512', int(setting['pressure_target'] * 100))
        self.plc.write('D514', int(setting['pressure_approx'] * 100))
        self.plc.write('D516', int(setting['pressure_thres_high'] * 100))
        self.plc.write('D518', int(setting['pressure_thres_low'] * 100))
        self.plc.write('D520', int(str(int(setting['pressure_hold_time'] * 10) + 3), base=16))
        self.plc.write('D522', int(str(int(setting['pumping_time'] * 10)), base=16))
        self.plc.write('D502', int(setting['silicate_count_total']))
        self.plc.write('D532', int(str(int(setting['pump_stop_timeout'])), base=16))
        self.plc.write('D534', int(str(int(setting['reserve1'] * 100)), base=10))
        self.plc.write('D536', int(str(int(setting['reserve2'] * 10)), base=16))

    def apply_plc_setting_to_ui(self, setting):
        try:
            # self.ui.pressure_coef_edit.setText(str(setting['pressure_coef']))
            self.ui.pressure_var_edit.setText(str(setting['pressure_var']))
            self.ui.pumping_time_edit.setText(str(setting['pumping_time']))
            self.ui.pressure_hold_time_edit.setText(str(setting['pressure_hold_time']))
            self.ui.pressure_thres_low_edit.setText(str(setting['pressure_thres_low']))
            self.ui.pressure_thres_high_edit.setText(str(setting['pressure_thres_high']))
            self.ui.pressure_approx_edit.setText(str(setting['pressure_approx']))
            self.ui.pressure_target_edit.setText(str(setting['pressure_target']))
            self.ui.silicate_count_total_edit.setText(str(int(setting['silicate_count_total'])))
            self.ui.pump_stop_timeout_edit.setText(str(int(setting['pump_stop_timeout'])))
            self.ui.variable_edit_0.setText(str(float(setting['reserve1'])))
            self.ui.variable_edit_1.setText(str(float(setting['reserve2'])))
        except:
            pass

    def update_pressure_threshold(self):
        self.chart.draw_threshold(self.setting['pressure_thres_low'], self.setting['pressure_thres_high'])

    def reset_clicked(self):
        self.plc.set('C180', 12)
        time.sleep(0.2)
        self.plc.clear('C180', 12)
        self.state = STATE_TO_RESET

    def auto_clicked(self):
        self.plc.set('C180', 10)
        time.sleep(0.2)
        self.plc.clear('C180', 10)

    def stop_clicked(self):
        self.plc.set('C180', 11)
        time.sleep(0.2)
        self.plc.clear('C180', 11)

    def save_setting_clicked(self):
        self.setting = self.get_setting_from_ui()
        self.apply_plc_setting_to_plc(self.setting)
        self.save_plc_setting(self.setting)
        self.update_pressure_threshold()

    def total_count_clear_clicked(self):
        self.plc.set('C180', 14)
        time.sleep(0.2)
        self.plc.clear('C180', 14)

    def silicate_count_current_clear_clicked(self):
        self.plc.set('C180', 15)
        time.sleep(0.2)
        self.plc.clear('C180', 15)

    def io_table_out_0_clicked(self):
        self.plc.set('C180', 0)
        time.sleep(0.2)
        self.plc.clear('C180', 0)

    def io_table_out_1_clicked(self):
        self.plc.set('C180', 1)
        time.sleep(0.2)
        self.plc.clear('C180', 1)

    def io_table_out_2_clicked(self):
        self.plc.set('C180', 2)
        time.sleep(0.2)
        self.plc.clear('C180', 2)

    def io_table_out_3_clicked(self):
        self.plc.set('C180', 3)
        time.sleep(0.2)
        self.plc.clear('C180', 3)

    def io_table_out_4_clicked(self):
        self.plc.set('C180', 4)
        time.sleep(0.2)
        self.plc.clear('C180', 4)

    def io_table_out_5_clicked(self):
        self.plc.set('C180', 5)
        time.sleep(0.2)
        self.plc.clear('C180', 5)

    def io_table_out_6_clicked(self):
        self.plc.set('C180', 6)
        time.sleep(0.2)
        self.plc.clear('C180', 6)

    def io_table_out_7_clicked(self):
        self.plc.set('C180', 7)
        time.sleep(0.2)
        self.plc.clear('C180', 7)

    def tab_changed(self, index):
        if self.plc_open:
            if index == self.ui.tabs.indexOf(self.ui.io_tab):
                self.io_table_timer.start()
            else:
                self.io_table_timer.stop()
            if index == self.ui.tabs.indexOf(self.ui.set_tab_2):
                self.debug_timer.start()
            else:
                self.debug_timer.stop()
        if index == self.ui.tabs.indexOf(self.ui.set_tab) or index == self.ui.tabs.indexOf(self.ui.set_tab_2):
            l = login.Login()
            if l.exec_() != QDialog.Accepted:
                self.ui.tabs.setCurrentWidget(self.ui.main_tab)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PressureUI()
    window.show()
    sys.exit(app.exec_())
