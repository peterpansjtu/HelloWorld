import sys

import matplotlib
from PyQt5.QtCore import QTimer, QRegExp
from PyQt5.QtWidgets import QDialog, QApplication, QGraphicsScene
from PyQt5.QtGui import QRegExpValidator
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import bar_code_recevce
import plc_control
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


class PressureUI(QDialog):
    def __init__(self):
        super(PressureUI, self).__init__()
        self.plc = None
        self.timestamp = []
        self.pressure = []
        self.max_pressure = 0
        self.bar_code = 0
        '''
        setup Qt UI
        '''
        self.ui = ui_main.Ui_Dialog()
        self.ui.setupUi(self)
        # TODO add input validator for ip address
        '''
        ipRange = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"  # Part of the regular expression
        # Regulare expression
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
        '''
        init pressure chart
        '''
        self.graphic_scene = QGraphicsScene()
        self.ui.pressure_view.setScene(self.graphic_scene)
        # FIXME: figure size should be handled better
        figure_size = (self.ui.pressure_view.width() / 110, self.ui.pressure_view.height() / 110)
        self.chart = PressureChart(figure_size)
        '''
        set up timer to check pressure periodically
        '''
        self.interval = 50
        self.timer = QTimer()
        self.timer.setSingleShot(False)
        self.timer.setInterval(self.interval)
        self.timer.timeout.connect(self.timeout)
        '''
        bar code receive setup
        '''
        self.bc_receive = None

    def bar_code_update(self, bar_code):
        self.bar_code = bar_code
        self.ui.dev_bar_code_browser.setText(self.bar_code)

    def timeout(self):
        if len(self.timestamp) > 0:
            self.timestamp.append(self.timestamp[-1] + self.interval / 1000.0)
        else:
            self.timestamp.append(0)
        value = self.plc.get(1)
        if value == -1:
            '''
            remove last item to keep timestamp and value consistent
            '''
            del self.timestamp[-1]
            self.timer.stop()
            self.ui.status_label.setText("断开")
            self.ui.status_label.setStyleSheet("font-size:48pt; font-weight:600; color:#ff0000")
            return
        value = 1 + value / 1000.0
        self.pressure.append(value)
        self.chart.draw_pressure(self.timestamp, self.pressure)
        self.graphic_scene.addWidget(self.chart)
        self.ui.pressure_view.show()
        self.ui.current_pressure_lcd.display(value)
        if value > self.max_pressure:
            self.max_pressure = value
            self.ui.max_pressure_lcd.display(value)

    def reset_clicked(self):
        self.plc.set(1, 0)

    def connect_clicked(self):
        plc_ip = self.ui.plc_ip_edit.text()
        plc_port = int(self.ui.plc_port_edit.text())
        print(plc_ip, plc_port)
        self.plc = plc_control.PLCControl(plc_ip, plc_port)
        if not self.plc.in_error():
            self.ui.status_label.setText("OK")
            self.ui.status_label.setStyleSheet("font-size:48pt; font-weight:600; color:#00ff00")
            self.timer.start()
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
            self.timer.stop()
            self.ui.status_label.setText("断开")
            self.ui.status_label.setStyleSheet("font-size:48pt; font-weight:600; color:#ff0000")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PressureUI()
    window.show()
    sys.exit(app.exec_())
