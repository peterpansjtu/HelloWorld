# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(977, 613)
        self.username_edit = QtWidgets.QLineEdit(Dialog)
        self.username_edit.setGeometry(QtCore.QRect(390, 110, 281, 61))
        self.username_edit.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.username_edit.setObjectName("username_edit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(270, 110, 101, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(270, 210, 101, 61))
        self.label_2.setObjectName("label_2")
        self.password_edit = QtWidgets.QLineEdit(Dialog)
        self.password_edit.setGeometry(QtCore.QRect(390, 210, 281, 61))
        self.password_edit.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.password_edit.setText("")
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_edit.setObjectName("password_edit")
        self.login_button = QtWidgets.QPushButton(Dialog)
        self.login_button.setGeometry(QtCore.QRect(240, 410, 211, 81))
        self.login_button.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.login_button.setObjectName("login_button")
        self.new_password_edit = QtWidgets.QLineEdit(Dialog)
        self.new_password_edit.setEnabled(False)
        self.new_password_edit.setGeometry(QtCore.QRect(390, 310, 281, 61))
        self.new_password_edit.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.new_password_edit.setText("")
        self.new_password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_password_edit.setObjectName("new_password_edit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(270, 310, 101, 61))
        self.label_3.setObjectName("label_3")
        self.new_password_check = QtWidgets.QCheckBox(Dialog)
        self.new_password_check.setGeometry(QtCore.QRect(710, 320, 171, 41))
        self.new_password_check.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.new_password_check.setChecked(False)
        self.new_password_check.setObjectName("new_password_check")
        self.change_password_button = QtWidgets.QPushButton(Dialog)
        self.change_password_button.setEnabled(False)
        self.change_password_button.setGeometry(QtCore.QRect(560, 410, 211, 81))
        self.change_password_button.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.change_password_button.setObjectName("change_password_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.username_edit.setText(_translate("Dialog", "admin"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt;\">用户名</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt;\">密码</span></p></body></html>"))
        self.login_button.setText(_translate("Dialog", "登录"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt;\">新密码</span></p></body></html>"))
        self.new_password_check.setText(_translate("Dialog", "修改密码"))
        self.change_password_button.setText(_translate("Dialog", "修改密码"))

