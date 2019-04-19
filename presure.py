import sys
from PyQt5.QtWidgets import QDialog, QApplication, QGraphicsScene
from PyQt5.QtCore import QTimer
import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import random

import ui_main
import plc_control

class Figure_Canvas(FigureCanvas):

    def __init__(self, size, parent = None, dpi = 100):
        self.figure = Figure(figsize = size, dpi = dpi)

        FigureCanvas.__init__(self, self.figure)
        self.setParent(parent)
        '''
        调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法
        '''
        self.axes = self.figure.add_subplot(111)
        self.x = []
        self.y = []
        self.axes.set_autoscaley_on(True)
        self.line, = self.axes.plot([], [])


    def update_presure(self, x, y):
        self.x.append(x)
        self.y.append(y)
        self.line.set_xdata(np.append(self.line.get_xdata(), x))
        self.line.set_ydata(np.append(self.line.get_ydata(), y))
        self.axes.relim()
        self.axes.autoscale_view()
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()

class presure_ui(QDialog):
    def __init__(self):
        super(presure_ui, self).__init__()

        self.plc = plc_control.plc_control('localhost', 12345)

        self.main_ui = ui_main.Ui_Dialog()
        self.main_ui.setupUi(self)

        self.main_ui.reset_button.clicked.connect(self.reset_clicked)

        self.graphicscene = QGraphicsScene()
        self.main_ui.pressure_view.setScene(self.graphicscene)
        '''
        FIXME: figure size should be handled better
        '''
        figure_size = (self.main_ui.pressure_view.width() / 110, self.main_ui.pressure_view.height() / 110)
        self.dr = Figure_Canvas(figure_size)

        self.x = 0;
        self.interval = 1000

        self.timer = QTimer()
        self.timer.setSingleShot(False)
        self.timer.setInterval(self.interval)
        self.timer.timeout.connect(self.timeout)
        self.timer.start()

    def timeout(self):
        self.x += int(self.interval / 1000)
        #y = random.randint(1, 10)
        y = self.plc.get(1)
        self.dr.update_presure(self.x, y)
        self.graphicscene.addWidget(self.dr)
        self.main_ui.pressure_view.show()

    def reset_clicked(self):
        self.plc.set(1, 0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = presure_ui()
    window.show()
    sys.exit(app.exec_())