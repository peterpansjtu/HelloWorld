import sys
import time
import matplotlib
from PyQt5.QtCore import QTimer, QRegExp
from PyQt5.QtWidgets import QDialog, QApplication, QGraphicsScene
from PyQt5.QtGui import QRegExpValidator
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import bar_code_recevce
import OmronFinsTcp
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
        self.line, = self.axes.plot([], [])

    def draw_pressure(self, x, y):
        self.line.set_xdata(x)
        self.line.set_ydata(y)
        self.axes.relim()
        self.axes.autoscale_view()
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()

warnings_dict = { 0 : '硅胶使用寿命已到，请及时更换!\n',
                  1 : '热保护跳闸，请手动复位\n',
                  2 : '急停中\n',
                  3 : '光栅异常\n',
                  4 : '没有读到条码\n',
                  5 : '重新开始请复位\n'
                }

manual_dict = { 0 : '真空泵手动中\n',
                1 : '下压缸手动中\n',
                2 : '阀1（快速阀）手动中\n',
                3 : '阀2（慢速阀）手动中\n',
                4 : '阀3（排气阀）手动中\n',
                5 : 'OK手动中\n',
                6 : 'NG手动中\n',
                7 : '蜂鸣器手动中\n',
                12 : '复位按钮\n',
                13 : '准备就绪（扫描枪&软件）\n',
                14 : '生产计数清零\n'
               }

class PressureUI(QDialog):
    def __init__(self):
        super(PressureUI, self).__init__()
        self.plc = OmronFinsTcp.OmronPLC()
        self.timestamp = []
        self.pressure = []
        self.max_pressure = 0
        self.bar_code = 0
        '''
        setup Qt UI
        '''
        self.ui = ui_main.Ui_Dialog()
        self.ui.setupUi(self)
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
        # TODO add input validator for ip address
        '''
        ipRange = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"  # Part of the regular expression
        # Regular expression
        ipRegex = QRegExp("^" + ipRange + "\\." + ipRange + "\\." + ipRange + "\\." + ipRange + "$")
        ipValidator = QRegExpValidator(ipRegex, self)
        self.ui.ip_line_edit.setValidator(ipValidator)
        #self.ui.ip_line_edit.setInputMask('000.000.000.000;_')
        '''
        '''
        register button click event
        '''
        self.ui.reset_button.clicked.connect(self.reset_clicked)
        self.ui.connect_button.clicked.connect(self.connect_clicked)
        self.ui.auto_button.clicked.connect(self.auto_clicked)
        self.ui.stop_button.clicked.connect(self.stop_clicked)
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
        '''
        set up timer to check device status periodically
        '''
        self.dev_status_interval = 500
        self.dev_status_timer = QTimer()
        self.dev_status_timer.setSingleShot(False)
        self.dev_status_timer.setInterval(self.dev_status_interval)
        self.dev_status_timer.timeout.connect(self.dev_status_timeout)
        '''
        set up timer to check pressure periodically
        '''
        self.pressure_interval = 50
        self.pressure_timer = QTimer()
        self.pressure_timer.setSingleShot(False)
        self.pressure_timer.setInterval(self.pressure_interval)
        self.pressure_timer.timeout.connect(self.pressure_timeout)
        '''
        set up timer to check device status periodically
        '''
        self.io_table_interval = 50
        self.io_table_timer = QTimer()
        self.io_table_timer.setSingleShot(False)
        self.io_table_timer.setInterval(self.io_table_interval)
        self.io_table_timer.timeout.connect(self.io_table_timeout)
        '''
        bar code receive setup
        '''
        self.bc_receive = None

    def bar_code_update(self, bar_code):
        self.bar_code = bar_code
        self.ui.dev_bar_code_browser.setText(self.bar_code)

    def dev_status_timeout(self):
        warnings = self.plc.read('C201')
        manual = self.plc.read('C203')
        print(manual)
        text = ''
        for bit in warnings_dict:
            if (warnings & 1 << bit):
                text += warnings_dict[bit]
        for bit in manual_dict:
            if (manual & 1 << bit):
                text += manual_dict[bit]
        self.ui.dev_info_browser.setText(text)
        self.ui.dev_info_browser.setStyleSheet("font-size:12pt; font-weight:600; color:#ff0000")

    def pressure_timeout(self):
        if len(self.timestamp) > 0:
            self.timestamp.append(self.timestamp[-1] + self.pressure_interval / 1000.0)
        else:
            self.timestamp.append(0)
        value = self.plc.read('D802')
        if value == -1:
            '''
            remove last item to keep timestamp and value consistent
            '''
            del self.timestamp[-1]
            self.pressure_timer.stop()
            self.ui.status_label.setText("断开")
            self.ui.status_label.setStyleSheet("font-size:48pt; font-weight:600; color:#ff0000")
            return
        #value = 1 + value / 1000.0
        self.pressure.append(value)
        self.chart.draw_pressure(self.timestamp, self.pressure)
        self.graphic_scene.addWidget(self.chart)
        self.ui.pressure_view.show()
        self.ui.current_pressure_lcd.display(value)
        if value > self.max_pressure:
            self.max_pressure = value
            self.ui.max_pressure_lcd.display(value)

    def io_table_timeout(self):
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

    def reset_clicked(self):
        self.plc.clear('C200', 0)

    def auto_clicked(self):
        self.plc.set('C200', 10)

    def stop_clicked(self):
        self.plc.set('C200', 11)

    def io_table_out_0_clicked(self):
        self.plc.set('C200', 0)
        time.sleep(0.2)
        self.plc.clear('C200', 0)

    def io_table_out_1_clicked(self):
        self.plc.set('C200', 1)
        time.sleep(0.2)
        self.plc.clear('C200', 1)

    def io_table_out_2_clicked(self):
        self.plc.set('C200', 2)
        time.sleep(0.2)
        self.plc.clear('C200', 2)

    def io_table_out_3_clicked(self):
        self.plc.set('C200', 3)
        time.sleep(0.2)
        self.plc.clear('C200', 3)

    def io_table_out_4_clicked(self):
        self.plc.set('C200', 4)
        time.sleep(0.2)
        self.plc.clear('C200', 4)

    def io_table_out_5_clicked(self):
        self.plc.set('C200', 5)
        time.sleep(0.2)
        self.plc.clear('C200', 5)

    def io_table_out_6_clicked(self):
        self.plc.set('C200', 6)
        time.sleep(0.2)
        self.plc.clear('C200', 6)

    def io_table_out_7_clicked(self):
        self.plc.set('C200', 7)
        time.sleep(0.2)
        self.plc.clear('C200', 7)

    def connect_clicked(self):
        plc_ip = self.ui.plc_ip_edit.text()
        plc_port = int(self.ui.plc_port_edit.text())
        print(plc_ip, plc_port)
        if self.plc.openFins(plc_ip, plc_port):
            self.ui.status_label.setText("OK")
            self.ui.status_label.setStyleSheet("font-size:48pt; font-weight:600; color:#00ff00")
            self.pressure_timer.start()
            self.dev_status_timer.start()
            self.io_table_timer.start()
            '''
            bar code receive setup
            '''
            bc_receive_ip = self.ui.local_ip_edit.text()
            bc_receive_port = int(self.ui.bc_receive_port_edit.text())
            print(bc_receive_ip, bc_receive_port)
            self.bc_receive = bar_code_recevce.BarCodeReceiveThread(bc_receive_ip, bc_receive_port)
            self.bc_receive.signal.connect(self.bar_code_update)
            self.bc_receive.start()
        else:
            self.pressure_timer.stop()
            self.ui.status_label.setText("断开")
            self.ui.status_label.setStyleSheet("font-size:48pt; font-weight:600; color:#ff0000")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PressureUI()
    window.show()
    sys.exit(app.exec_())
