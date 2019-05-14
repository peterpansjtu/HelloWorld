# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1007, 671)
        self.tabs = QtWidgets.QTabWidget(Dialog)
        self.tabs.setGeometry(QtCore.QRect(0, 0, 1391, 891))
        self.tabs.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.tabs.setObjectName("tabs")
        self.main_tab = QtWidgets.QWidget()
        self.main_tab.setObjectName("main_tab")
        self.pressure_view = QtWidgets.QGraphicsView(self.main_tab)
        self.pressure_view.setGeometry(QtCore.QRect(400, 90, 591, 411))
        self.pressure_view.setObjectName("pressure_view")
        self.label = QtWidgets.QLabel(self.main_tab)
        self.label.setGeometry(QtCore.QRect(430, 30, 141, 31))
        self.label.setObjectName("label")
        self.variable_label_0 = QtWidgets.QLabel(self.main_tab)
        self.variable_label_0.setGeometry(QtCore.QRect(730, 30, 141, 31))
        self.variable_label_0.setStyleSheet("font-size:11pt; font-weight:600; color:#ff5500;")
        self.variable_label_0.setObjectName("variable_label_0")
        self.reset_button = QtWidgets.QPushButton(self.main_tab)
        self.reset_button.setGeometry(QtCore.QRect(70, 400, 191, 71))
        self.reset_button.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.reset_button.setObjectName("reset_button")
        self.auto_button = QtWidgets.QPushButton(self.main_tab)
        self.auto_button.setGeometry(QtCore.QRect(70, 480, 191, 71))
        self.auto_button.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.auto_button.setObjectName("auto_button")
        self.stop_button = QtWidgets.QPushButton(self.main_tab)
        self.stop_button.setGeometry(QtCore.QRect(70, 560, 191, 71))
        self.stop_button.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.stop_button.setObjectName("stop_button")
        self.label_3 = QtWidgets.QLabel(self.main_tab)
        self.label_3.setGeometry(QtCore.QRect(10, 350, 81, 21))
        self.label_3.setObjectName("label_3")
        self.dev_bar_code_browser = QtWidgets.QTextBrowser(self.main_tab)
        self.dev_bar_code_browser.setGeometry(QtCore.QRect(90, 340, 301, 51))
        self.dev_bar_code_browser.setObjectName("dev_bar_code_browser")
        self.status_label = QtWidgets.QLabel(self.main_tab)
        self.status_label.setGeometry(QtCore.QRect(90, 30, 151, 51))
        self.status_label.setObjectName("status_label")
        self.label_6 = QtWidgets.QLabel(self.main_tab)
        self.label_6.setGeometry(QtCore.QRect(20, 120, 31, 131))
        self.label_6.setObjectName("label_6")
        self.dev_info_browser = QtWidgets.QTextBrowser(self.main_tab)
        self.dev_info_browser.setGeometry(QtCore.QRect(50, 100, 291, 221))
        self.dev_info_browser.setObjectName("dev_info_browser")
        self.current_pressure_lcd = QtWidgets.QLCDNumber(self.main_tab)
        self.current_pressure_lcd.setGeometry(QtCore.QRect(580, 20, 131, 51))
        self.current_pressure_lcd.setObjectName("current_pressure_lcd")
        self.max_pressure_lcd = QtWidgets.QLCDNumber(self.main_tab)
        self.max_pressure_lcd.setGeometry(QtCore.QRect(860, 20, 131, 51))
        self.max_pressure_lcd.setObjectName("max_pressure_lcd")
        self.label_4 = QtWidgets.QLabel(self.main_tab)
        self.label_4.setGeometry(QtCore.QRect(510, 530, 121, 31))
        self.label_4.setObjectName("label_4")
        self.total_count_lcd = QtWidgets.QLCDNumber(self.main_tab)
        self.total_count_lcd.setGeometry(QtCore.QRect(630, 520, 201, 51))
        self.total_count_lcd.setObjectName("total_count_lcd")
        self.total_count_clear_button = QtWidgets.QPushButton(self.main_tab)
        self.total_count_clear_button.setGeometry(QtCore.QRect(870, 520, 121, 51))
        self.total_count_clear_button.setObjectName("total_count_clear_button")
        self.connection_label = QtWidgets.QLabel(self.main_tab)
        self.connection_label.setGeometry(QtCore.QRect(660, 590, 301, 41))
        self.connection_label.setObjectName("connection_label")
        self.tabs.addTab(self.main_tab, "")
        self.io_tab = QtWidgets.QWidget()
        self.io_tab.setObjectName("io_tab")
        self.input_frame = QtWidgets.QFrame(self.io_tab)
        self.input_frame.setGeometry(QtCore.QRect(80, 100, 451, 501))
        self.input_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.input_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input_frame.setObjectName("input_frame")
        self.label_5 = QtWidgets.QLabel(self.input_frame)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 91, 31))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.input_frame)
        self.label_7.setGeometry(QtCore.QRect(30, 60, 55, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.input_frame)
        self.label_8.setGeometry(QtCore.QRect(30, 100, 55, 16))
        self.label_8.setObjectName("label_8")
        self.label_12 = QtWidgets.QLabel(self.input_frame)
        self.label_12.setGeometry(QtCore.QRect(90, 60, 241, 21))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.input_frame)
        self.label_13.setGeometry(QtCore.QRect(90, 100, 241, 21))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.input_frame)
        self.label_14.setGeometry(QtCore.QRect(90, 180, 241, 21))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.input_frame)
        self.label_15.setGeometry(QtCore.QRect(30, 140, 55, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.input_frame)
        self.label_16.setGeometry(QtCore.QRect(30, 180, 55, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.input_frame)
        self.label_17.setGeometry(QtCore.QRect(90, 140, 241, 21))
        self.label_17.setObjectName("label_17")
        self.label_32 = QtWidgets.QLabel(self.input_frame)
        self.label_32.setGeometry(QtCore.QRect(90, 260, 241, 21))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.input_frame)
        self.label_33.setGeometry(QtCore.QRect(90, 220, 241, 21))
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.input_frame)
        self.label_34.setGeometry(QtCore.QRect(90, 340, 241, 21))
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.input_frame)
        self.label_35.setGeometry(QtCore.QRect(90, 300, 241, 21))
        self.label_35.setObjectName("label_35")
        self.label_9 = QtWidgets.QLabel(self.input_frame)
        self.label_9.setGeometry(QtCore.QRect(30, 260, 55, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.input_frame)
        self.label_10.setGeometry(QtCore.QRect(30, 220, 55, 16))
        self.label_10.setObjectName("label_10")
        self.label_36 = QtWidgets.QLabel(self.input_frame)
        self.label_36.setGeometry(QtCore.QRect(30, 300, 55, 16))
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.input_frame)
        self.label_37.setGeometry(QtCore.QRect(30, 340, 55, 16))
        self.label_37.setObjectName("label_37")
        self.io_table_in_label_7 = QtWidgets.QLabel(self.input_frame)
        self.io_table_in_label_7.setGeometry(QtCore.QRect(180, 340, 55, 16))
        self.io_table_in_label_7.setStyleSheet("QLabel {background-color: black}")
        self.io_table_in_label_7.setText("")
        self.io_table_in_label_7.setObjectName("io_table_in_label_7")
        self.io_table_in_label_6 = QtWidgets.QLabel(self.input_frame)
        self.io_table_in_label_6.setGeometry(QtCore.QRect(180, 300, 55, 16))
        self.io_table_in_label_6.setStyleSheet("QLabel {background-color: black}")
        self.io_table_in_label_6.setText("")
        self.io_table_in_label_6.setObjectName("io_table_in_label_6")
        self.io_table_in_label_5 = QtWidgets.QLabel(self.input_frame)
        self.io_table_in_label_5.setGeometry(QtCore.QRect(180, 260, 55, 16))
        self.io_table_in_label_5.setStyleSheet("QLabel {background-color: black}")
        self.io_table_in_label_5.setText("")
        self.io_table_in_label_5.setObjectName("io_table_in_label_5")
        self.io_table_in_label_4 = QtWidgets.QLabel(self.input_frame)
        self.io_table_in_label_4.setGeometry(QtCore.QRect(180, 220, 55, 16))
        self.io_table_in_label_4.setStyleSheet("QLabel {background-color: black}")
        self.io_table_in_label_4.setText("")
        self.io_table_in_label_4.setObjectName("io_table_in_label_4")
        self.io_table_in_label_0 = QtWidgets.QLabel(self.input_frame)
        self.io_table_in_label_0.setGeometry(QtCore.QRect(180, 60, 55, 16))
        self.io_table_in_label_0.setStyleSheet("QLabel {background-color: black}")
        self.io_table_in_label_0.setText("")
        self.io_table_in_label_0.setObjectName("io_table_in_label_0")
        self.io_table_in_label_2 = QtWidgets.QLabel(self.input_frame)
        self.io_table_in_label_2.setGeometry(QtCore.QRect(180, 140, 55, 16))
        self.io_table_in_label_2.setStyleSheet("QLabel {background-color: black}")
        self.io_table_in_label_2.setText("")
        self.io_table_in_label_2.setObjectName("io_table_in_label_2")
        self.io_table_in_label_3 = QtWidgets.QLabel(self.input_frame)
        self.io_table_in_label_3.setGeometry(QtCore.QRect(180, 180, 55, 16))
        self.io_table_in_label_3.setStyleSheet("QLabel {background-color: black}")
        self.io_table_in_label_3.setText("")
        self.io_table_in_label_3.setObjectName("io_table_in_label_3")
        self.io_table_in_label_1 = QtWidgets.QLabel(self.input_frame)
        self.io_table_in_label_1.setGeometry(QtCore.QRect(180, 100, 55, 16))
        self.io_table_in_label_1.setStyleSheet("QLabel {background-color: black}")
        self.io_table_in_label_1.setText("")
        self.io_table_in_label_1.setObjectName("io_table_in_label_1")
        self.input_frame_2 = QtWidgets.QFrame(self.io_tab)
        self.input_frame_2.setGeometry(QtCore.QRect(510, 100, 451, 501))
        self.input_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.input_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.input_frame_2.setObjectName("input_frame_2")
        self.label_18 = QtWidgets.QLabel(self.input_frame_2)
        self.label_18.setGeometry(QtCore.QRect(20, 10, 91, 31))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.input_frame_2)
        self.label_19.setGeometry(QtCore.QRect(30, 60, 55, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.input_frame_2)
        self.label_20.setGeometry(QtCore.QRect(30, 100, 55, 16))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.input_frame_2)
        self.label_21.setGeometry(QtCore.QRect(90, 60, 241, 21))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.input_frame_2)
        self.label_22.setGeometry(QtCore.QRect(90, 100, 241, 21))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.input_frame_2)
        self.label_23.setGeometry(QtCore.QRect(90, 180, 241, 21))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.input_frame_2)
        self.label_24.setGeometry(QtCore.QRect(30, 140, 55, 16))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.input_frame_2)
        self.label_25.setGeometry(QtCore.QRect(30, 180, 55, 16))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.input_frame_2)
        self.label_26.setGeometry(QtCore.QRect(90, 140, 241, 21))
        self.label_26.setObjectName("label_26")
        self.io_table_out_button_0 = QtWidgets.QPushButton(self.input_frame_2)
        self.io_table_out_button_0.setGeometry(QtCore.QRect(330, 50, 41, 28))
        self.io_table_out_button_0.setText("")
        self.io_table_out_button_0.setObjectName("io_table_out_button_0")
        self.io_table_out_button_1 = QtWidgets.QPushButton(self.input_frame_2)
        self.io_table_out_button_1.setGeometry(QtCore.QRect(330, 90, 41, 28))
        self.io_table_out_button_1.setText("")
        self.io_table_out_button_1.setObjectName("io_table_out_button_1")
        self.io_table_out_button_2 = QtWidgets.QPushButton(self.input_frame_2)
        self.io_table_out_button_2.setGeometry(QtCore.QRect(330, 130, 41, 28))
        self.io_table_out_button_2.setText("")
        self.io_table_out_button_2.setObjectName("io_table_out_button_2")
        self.io_table_out_button_3 = QtWidgets.QPushButton(self.input_frame_2)
        self.io_table_out_button_3.setGeometry(QtCore.QRect(330, 170, 41, 28))
        self.io_table_out_button_3.setText("")
        self.io_table_out_button_3.setObjectName("io_table_out_button_3")
        self.io_table_out_label_3 = QtWidgets.QLabel(self.input_frame_2)
        self.io_table_out_label_3.setGeometry(QtCore.QRect(240, 180, 55, 16))
        self.io_table_out_label_3.setStyleSheet("QLabel {background-color: black}")
        self.io_table_out_label_3.setText("")
        self.io_table_out_label_3.setObjectName("io_table_out_label_3")
        self.io_table_out_label_1 = QtWidgets.QLabel(self.input_frame_2)
        self.io_table_out_label_1.setGeometry(QtCore.QRect(240, 100, 55, 16))
        self.io_table_out_label_1.setStyleSheet("QLabel {background-color: black}")
        self.io_table_out_label_1.setText("")
        self.io_table_out_label_1.setObjectName("io_table_out_label_1")
        self.io_table_out_label_0 = QtWidgets.QLabel(self.input_frame_2)
        self.io_table_out_label_0.setGeometry(QtCore.QRect(240, 60, 55, 16))
        self.io_table_out_label_0.setStyleSheet("QLabel {background-color: black}")
        self.io_table_out_label_0.setText("")
        self.io_table_out_label_0.setObjectName("io_table_out_label_0")
        self.io_table_out_label_2 = QtWidgets.QLabel(self.input_frame_2)
        self.io_table_out_label_2.setGeometry(QtCore.QRect(240, 140, 55, 16))
        self.io_table_out_label_2.setStyleSheet("QLabel {background-color: black}")
        self.io_table_out_label_2.setText("")
        self.io_table_out_label_2.setObjectName("io_table_out_label_2")
        self.label_54 = QtWidgets.QLabel(self.input_frame_2)
        self.label_54.setGeometry(QtCore.QRect(30, 340, 55, 16))
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(self.input_frame_2)
        self.label_55.setGeometry(QtCore.QRect(90, 220, 241, 21))
        self.label_55.setObjectName("label_55")
        self.io_table_out_button_6 = QtWidgets.QPushButton(self.input_frame_2)
        self.io_table_out_button_6.setGeometry(QtCore.QRect(330, 290, 41, 28))
        self.io_table_out_button_6.setText("")
        self.io_table_out_button_6.setObjectName("io_table_out_button_6")
        self.label_56 = QtWidgets.QLabel(self.input_frame_2)
        self.label_56.setGeometry(QtCore.QRect(90, 340, 241, 21))
        self.label_56.setObjectName("label_56")
        self.label_57 = QtWidgets.QLabel(self.input_frame_2)
        self.label_57.setGeometry(QtCore.QRect(30, 220, 55, 16))
        self.label_57.setObjectName("label_57")
        self.io_table_out_label_5 = QtWidgets.QLabel(self.input_frame_2)
        self.io_table_out_label_5.setGeometry(QtCore.QRect(240, 260, 55, 16))
        self.io_table_out_label_5.setStyleSheet("QLabel {background-color: black}")
        self.io_table_out_label_5.setText("")
        self.io_table_out_label_5.setObjectName("io_table_out_label_5")
        self.io_table_out_label_7 = QtWidgets.QLabel(self.input_frame_2)
        self.io_table_out_label_7.setGeometry(QtCore.QRect(240, 340, 55, 16))
        self.io_table_out_label_7.setStyleSheet("QLabel {background-color: black}")
        self.io_table_out_label_7.setText("")
        self.io_table_out_label_7.setObjectName("io_table_out_label_7")
        self.io_table_out_label_4 = QtWidgets.QLabel(self.input_frame_2)
        self.io_table_out_label_4.setGeometry(QtCore.QRect(240, 220, 55, 16))
        self.io_table_out_label_4.setStyleSheet("QLabel {background-color: black}")
        self.io_table_out_label_4.setText("")
        self.io_table_out_label_4.setObjectName("io_table_out_label_4")
        self.io_table_out_button_4 = QtWidgets.QPushButton(self.input_frame_2)
        self.io_table_out_button_4.setGeometry(QtCore.QRect(330, 210, 41, 28))
        self.io_table_out_button_4.setText("")
        self.io_table_out_button_4.setObjectName("io_table_out_button_4")
        self.io_table_out_label_6 = QtWidgets.QLabel(self.input_frame_2)
        self.io_table_out_label_6.setGeometry(QtCore.QRect(240, 300, 55, 16))
        self.io_table_out_label_6.setStyleSheet("QLabel {background-color: black}")
        self.io_table_out_label_6.setText("")
        self.io_table_out_label_6.setObjectName("io_table_out_label_6")
        self.label_63 = QtWidgets.QLabel(self.input_frame_2)
        self.label_63.setGeometry(QtCore.QRect(30, 260, 55, 16))
        self.label_63.setObjectName("label_63")
        self.io_table_out_button_5 = QtWidgets.QPushButton(self.input_frame_2)
        self.io_table_out_button_5.setGeometry(QtCore.QRect(330, 250, 41, 28))
        self.io_table_out_button_5.setText("")
        self.io_table_out_button_5.setObjectName("io_table_out_button_5")
        self.label_64 = QtWidgets.QLabel(self.input_frame_2)
        self.label_64.setGeometry(QtCore.QRect(30, 300, 55, 16))
        self.label_64.setObjectName("label_64")
        self.io_table_out_button_7 = QtWidgets.QPushButton(self.input_frame_2)
        self.io_table_out_button_7.setGeometry(QtCore.QRect(330, 330, 41, 28))
        self.io_table_out_button_7.setText("")
        self.io_table_out_button_7.setObjectName("io_table_out_button_7")
        self.label_65 = QtWidgets.QLabel(self.input_frame_2)
        self.label_65.setGeometry(QtCore.QRect(90, 260, 241, 21))
        self.label_65.setObjectName("label_65")
        self.label_66 = QtWidgets.QLabel(self.input_frame_2)
        self.label_66.setGeometry(QtCore.QRect(90, 300, 241, 21))
        self.label_66.setObjectName("label_66")
        self.label_66.raise_()
        self.label_65.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.label_25.raise_()
        self.label_26.raise_()
        self.io_table_out_button_0.raise_()
        self.io_table_out_button_1.raise_()
        self.io_table_out_button_2.raise_()
        self.io_table_out_button_3.raise_()
        self.io_table_out_label_3.raise_()
        self.io_table_out_label_1.raise_()
        self.io_table_out_label_0.raise_()
        self.io_table_out_label_2.raise_()
        self.label_54.raise_()
        self.label_55.raise_()
        self.io_table_out_button_6.raise_()
        self.label_56.raise_()
        self.label_57.raise_()
        self.io_table_out_label_5.raise_()
        self.io_table_out_label_7.raise_()
        self.io_table_out_label_4.raise_()
        self.io_table_out_button_4.raise_()
        self.io_table_out_label_6.raise_()
        self.label_63.raise_()
        self.io_table_out_button_5.raise_()
        self.label_64.raise_()
        self.io_table_out_button_7.raise_()
        self.tabs.addTab(self.io_tab, "")
        self.set_tab = QtWidgets.QWidget()
        self.set_tab.setObjectName("set_tab")
        self.frame = QtWidgets.QFrame(self.set_tab)
        self.frame.setGeometry(QtCore.QRect(60, -10, 791, 641))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_27 = QtWidgets.QLabel(self.frame)
        self.label_27.setGeometry(QtCore.QRect(40, 30, 111, 51))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.frame)
        self.label_28.setGeometry(QtCore.QRect(120, 110, 111, 41))
        self.label_28.setObjectName("label_28")
        self.pressure_coef_edit = QtWidgets.QLineEdit(self.frame)
        self.pressure_coef_edit.setGeometry(QtCore.QRect(280, 110, 131, 31))
        self.pressure_coef_edit.setObjectName("pressure_coef_edit")
        self.label_67 = QtWidgets.QLabel(self.frame)
        self.label_67.setGeometry(QtCore.QRect(480, 110, 111, 41))
        self.label_67.setObjectName("label_67")
        self.pressure_var_edit = QtWidgets.QLineEdit(self.frame)
        self.pressure_var_edit.setGeometry(QtCore.QRect(640, 110, 131, 31))
        self.pressure_var_edit.setObjectName("pressure_var_edit")
        self.label_68 = QtWidgets.QLabel(self.frame)
        self.label_68.setGeometry(QtCore.QRect(120, 190, 111, 41))
        self.label_68.setObjectName("label_68")
        self.pumping_time_edit = QtWidgets.QLineEdit(self.frame)
        self.pumping_time_edit.setGeometry(QtCore.QRect(280, 190, 131, 31))
        self.pumping_time_edit.setObjectName("pumping_time_edit")
        self.pressure_hold_time_edit = QtWidgets.QLineEdit(self.frame)
        self.pressure_hold_time_edit.setGeometry(QtCore.QRect(640, 190, 131, 31))
        self.pressure_hold_time_edit.setObjectName("pressure_hold_time_edit")
        self.label_69 = QtWidgets.QLabel(self.frame)
        self.label_69.setGeometry(QtCore.QRect(480, 190, 111, 41))
        self.label_69.setObjectName("label_69")
        self.label_70 = QtWidgets.QLabel(self.frame)
        self.label_70.setGeometry(QtCore.QRect(120, 270, 141, 41))
        self.label_70.setObjectName("label_70")
        self.pressure_thres_low_edit = QtWidgets.QLineEdit(self.frame)
        self.pressure_thres_low_edit.setGeometry(QtCore.QRect(280, 270, 131, 31))
        self.pressure_thres_low_edit.setObjectName("pressure_thres_low_edit")
        self.label_71 = QtWidgets.QLabel(self.frame)
        self.label_71.setGeometry(QtCore.QRect(480, 350, 141, 41))
        self.label_71.setObjectName("label_71")
        self.pressure_thres_high_edit = QtWidgets.QLineEdit(self.frame)
        self.pressure_thres_high_edit.setGeometry(QtCore.QRect(640, 270, 131, 31))
        self.pressure_thres_high_edit.setObjectName("pressure_thres_high_edit")
        self.pressure_approx_edit = QtWidgets.QLineEdit(self.frame)
        self.pressure_approx_edit.setGeometry(QtCore.QRect(280, 350, 131, 31))
        self.pressure_approx_edit.setObjectName("pressure_approx_edit")
        self.label_72 = QtWidgets.QLabel(self.frame)
        self.label_72.setGeometry(QtCore.QRect(480, 270, 141, 41))
        self.label_72.setObjectName("label_72")
        self.label_73 = QtWidgets.QLabel(self.frame)
        self.label_73.setGeometry(QtCore.QRect(120, 350, 141, 41))
        self.label_73.setObjectName("label_73")
        self.pressure_target_edit = QtWidgets.QLineEdit(self.frame)
        self.pressure_target_edit.setGeometry(QtCore.QRect(640, 350, 131, 31))
        self.pressure_target_edit.setObjectName("pressure_target_edit")
        self.save_setting_button = QtWidgets.QPushButton(self.frame)
        self.save_setting_button.setGeometry(QtCore.QRect(390, 580, 161, 51))
        self.save_setting_button.setObjectName("save_setting_button")
        self.label_74 = QtWidgets.QLabel(self.frame)
        self.label_74.setGeometry(QtCore.QRect(120, 490, 211, 41))
        self.label_74.setObjectName("label_74")
        self.label_75 = QtWidgets.QLabel(self.frame)
        self.label_75.setGeometry(QtCore.QRect(120, 420, 231, 41))
        self.label_75.setObjectName("label_75")
        self.silicate_count_total_edit = QtWidgets.QLineEdit(self.frame)
        self.silicate_count_total_edit.setGeometry(QtCore.QRect(360, 420, 131, 31))
        self.silicate_count_total_edit.setObjectName("silicate_count_total_edit")
        self.silicate_count_current_clear_button = QtWidgets.QPushButton(self.frame)
        self.silicate_count_current_clear_button.setGeometry(QtCore.QRect(550, 480, 121, 51))
        self.silicate_count_current_clear_button.setObjectName("silicate_count_current_clear_button")
        self.silicate_count_current_lcd = QtWidgets.QLCDNumber(self.frame)
        self.silicate_count_current_lcd.setGeometry(QtCore.QRect(330, 480, 201, 51))
        self.silicate_count_current_lcd.setObjectName("silicate_count_current_lcd")
        self.tabs.addTab(self.set_tab, "")
        self.network_tab = QtWidgets.QWidget()
        self.network_tab.setObjectName("network_tab")
        self.label_59 = QtWidgets.QLabel(self.network_tab)
        self.label_59.setGeometry(QtCore.QRect(280, 250, 101, 31))
        self.label_59.setObjectName("label_59")
        self.code_scannner_ip_edit = QtWidgets.QLineEdit(self.network_tab)
        self.code_scannner_ip_edit.setGeometry(QtCore.QRect(370, 240, 111, 51))
        self.code_scannner_ip_edit.setObjectName("code_scannner_ip_edit")
        self.plc_ip_edit = QtWidgets.QLineEdit(self.network_tab)
        self.plc_ip_edit.setGeometry(QtCore.QRect(370, 140, 111, 51))
        self.plc_ip_edit.setObjectName("plc_ip_edit")
        self.label_60 = QtWidgets.QLabel(self.network_tab)
        self.label_60.setGeometry(QtCore.QRect(280, 150, 101, 31))
        self.label_60.setObjectName("label_60")
        self.code_scanner_port_edit = QtWidgets.QLineEdit(self.network_tab)
        self.code_scanner_port_edit.setGeometry(QtCore.QRect(620, 240, 51, 51))
        self.code_scanner_port_edit.setObjectName("code_scanner_port_edit")
        self.label_61 = QtWidgets.QLabel(self.network_tab)
        self.label_61.setGeometry(QtCore.QRect(540, 250, 81, 31))
        self.label_61.setObjectName("label_61")
        self.plc_port_edit = QtWidgets.QLineEdit(self.network_tab)
        self.plc_port_edit.setGeometry(QtCore.QRect(620, 140, 51, 51))
        self.plc_port_edit.setObjectName("plc_port_edit")
        self.label_62 = QtWidgets.QLabel(self.network_tab)
        self.label_62.setGeometry(QtCore.QRect(540, 150, 71, 31))
        self.label_62.setObjectName("label_62")
        self.tabs.addTab(self.network_tab, "")

        self.retranslateUi(Dialog)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ff5500;\">当前负压(Kpa):</span></p></body></html>"))
        self.variable_label_0.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ff5500;\">最大负压(Kpa):</span></p></body></html>"))
        self.reset_button.setText(_translate("Dialog", "复位"))
        self.auto_button.setText(_translate("Dialog", "自动"))
        self.stop_button.setText(_translate("Dialog", "停止"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">当前条形码</span></p></body></html>"))
        self.status_label.setText(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">设</span></p><p><span style=\" font-size:12pt; font-weight:600;\">备</span></p><p><span style=\" font-size:12pt; font-weight:600;\">信</span></p><p><span style=\" font-size:12pt; font-weight:600;\">息</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">生产计数</span></p></body></html>"))
        self.total_count_clear_button.setText(_translate("Dialog", "清零"))
        self.connection_label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">连接中</span></p></body></html>"))
        self.tabs.setTabText(self.tabs.indexOf(self.main_tab), _translate("Dialog", "主界面"))
        self.label_5.setText(_translate("Dialog", "输入"))
        self.label_7.setText(_translate("Dialog", "00.00"))
        self.label_8.setText(_translate("Dialog", "00.01"))
        self.label_12.setText(_translate("Dialog", "<html><head/><body><p>启动</p></body></html>"))
        self.label_13.setText(_translate("Dialog", "急停"))
        self.label_14.setText(_translate("Dialog", "光栅"))
        self.label_15.setText(_translate("Dialog", "00.02"))
        self.label_16.setText(_translate("Dialog", "00.03"))
        self.label_17.setText(_translate("Dialog", "热过载"))
        self.label_32.setText(_translate("Dialog", "备用"))
        self.label_33.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">备用</span></p></body></html>"))
        self.label_34.setText(_translate("Dialog", "备用"))
        self.label_35.setText(_translate("Dialog", "备用"))
        self.label_9.setText(_translate("Dialog", "00.05"))
        self.label_10.setText(_translate("Dialog", "00.04"))
        self.label_36.setText(_translate("Dialog", "00.06"))
        self.label_37.setText(_translate("Dialog", "00.07"))
        self.label_18.setText(_translate("Dialog", "输出"))
        self.label_19.setText(_translate("Dialog", "100.00"))
        self.label_20.setText(_translate("Dialog", "100.01"))
        self.label_21.setText(_translate("Dialog", "真空泵"))
        self.label_22.setText(_translate("Dialog", "下压缸"))
        self.label_23.setText(_translate("Dialog", "阀2（慢速阀）"))
        self.label_24.setText(_translate("Dialog", "100.02"))
        self.label_25.setText(_translate("Dialog", "100.03"))
        self.label_26.setText(_translate("Dialog", "阀1（快速阀）"))
        self.label_54.setText(_translate("Dialog", "100.07"))
        self.label_55.setText(_translate("Dialog", "阀3（排气阀）"))
        self.label_56.setText(_translate("Dialog", "蜂鸣器"))
        self.label_57.setText(_translate("Dialog", "100.04"))
        self.label_63.setText(_translate("Dialog", "100.05"))
        self.label_64.setText(_translate("Dialog", "100.06"))
        self.label_65.setText(_translate("Dialog", "OK"))
        self.label_66.setText(_translate("Dialog", "NG"))
        self.tabs.setTabText(self.tabs.indexOf(self.io_tab), _translate("Dialog", "输入/输出"))
        self.label_27.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">设定</span></p></body></html>"))
        self.label_28.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt;\">压力系数</span></p></body></html>"))
        self.pressure_coef_edit.setText(_translate("Dialog", "1.1"))
        self.label_67.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt;\">压力偏差</span></p></body></html>"))
        self.pressure_var_edit.setText(_translate("Dialog", "0.2"))
        self.label_68.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt;\">抽气时间</span></p></body></html>"))
        self.pumping_time_edit.setText(_translate("Dialog", "0.5"))
        self.pressure_hold_time_edit.setText(_translate("Dialog", "3.2"))
        self.label_69.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt;\">保压时间</span></p></body></html>"))
        self.label_70.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt;\">压力下限值</span></p></body></html>"))
        self.pressure_thres_low_edit.setText(_translate("Dialog", "40.0"))
        self.label_71.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt;\">负压目标值</span></p></body></html>"))
        self.pressure_thres_high_edit.setText(_translate("Dialog", "35"))
        self.pressure_approx_edit.setText(_translate("Dialog", "30"))
        self.label_72.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt;\">压力上限值</span></p></body></html>"))
        self.label_73.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt;\">负压接近值</span></p></body></html>"))
        self.pressure_target_edit.setText(_translate("Dialog", "37.5"))
        self.save_setting_button.setText(_translate("Dialog", "保存"))
        self.label_74.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt;\">硅胶已使用次数</span></p></body></html>"))
        self.label_75.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt;\">硅胶寿命次数设定</span></p></body></html>"))
        self.silicate_count_total_edit.setText(_translate("Dialog", "10000"))
        self.silicate_count_current_clear_button.setText(_translate("Dialog", "清零"))
        self.tabs.setTabText(self.tabs.indexOf(self.set_tab), _translate("Dialog", "参数设定"))
        self.label_59.setText(_translate("Dialog", "<html><head/><body><p>扫码枪地址</p></body></html>"))
        self.code_scannner_ip_edit.setText(_translate("Dialog", "192.168.0.100"))
        self.plc_ip_edit.setText(_translate("Dialog", "192.168.0.10"))
        self.label_60.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">PLC地址</span></p></body></html>"))
        self.code_scanner_port_edit.setText(_translate("Dialog", "2001"))
        self.label_61.setText(_translate("Dialog", "<html><head/><body><p>扫码枪端口</p></body></html>"))
        self.plc_port_edit.setText(_translate("Dialog", "9600"))
        self.label_62.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">PLC端口</span></p></body></html>"))
        self.tabs.setTabText(self.tabs.indexOf(self.network_tab), _translate("Dialog", "网络设定"))


