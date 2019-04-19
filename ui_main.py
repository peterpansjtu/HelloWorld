# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1389, 894)
        self.tabs = QtWidgets.QTabWidget(Dialog)
        self.tabs.setGeometry(QtCore.QRect(0, 0, 1391, 891))
        self.tabs.setObjectName("tabs")
        self.main_tab = QtWidgets.QWidget()
        self.main_tab.setObjectName("main_tab")
        self.pressure_view = QtWidgets.QGraphicsView(self.main_tab)
        self.pressure_view.setGeometry(QtCore.QRect(580, 60, 791, 551))
        self.pressure_view.setObjectName("pressure_view")
        self.tabs.addTab(self.main_tab, "")
        self.io_tab = QtWidgets.QWidget()
        self.io_tab.setObjectName("io_tab")
        self.tabs.addTab(self.io_tab, "")
        self.set_tab = QtWidgets.QWidget()
        self.set_tab.setObjectName("set_tab")
        self.tabs.addTab(self.set_tab, "")

        self.retranslateUi(Dialog)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.tabs.setTabText(self.tabs.indexOf(self.main_tab), _translate("Dialog", "主界面"))
        self.tabs.setTabText(self.tabs.indexOf(self.io_tab), _translate("Dialog", "输入/输出"))
        self.tabs.setTabText(self.tabs.indexOf(self.set_tab), _translate("Dialog", "参数设定"))

