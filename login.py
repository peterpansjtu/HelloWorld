import os
from hashlib import md5

from PyQt5 import QtWidgets, QtCore

import ui_login


class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.ui = ui_login.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.login_button.clicked.connect(self.handleLogin)
        self.ui.new_password_check.stateChanged.connect(self.new_password_clicked)
        self.ui.change_password_button.clicked.connect(self.change_password_clicked)

    def password_match(self):
        password_in = self.ui.password_edit.text()
        password_in = md5(password_in.encode()).hexdigest()
        password = md5('admin'.encode()).hexdigest()
        if os.path.isfile('密码.txt'):
            with open('密码.txt', 'r', encoding='utf8') as f:
                lines = f.read().splitlines()
                if len(lines) == 1:
                    [password] = lines
        return password_in == password

    def handleLogin(self):
        username_in = self.ui.username_edit.text()
        if self.password_match():
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Error', username_in + '的密码不正确')

    def change_password_clicked(self):
        new_password = self.ui.new_password_edit.text()
        new_password = md5(new_password.encode()).hexdigest()
        if self.password_match():
            with open('密码.txt', 'w', encoding='utf8', newline='') as f:
                f.write(new_password)
            QtWidgets.QMessageBox.information(
                self, 'OK', '密码修改成功')
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Error', '旧密码不正确')

    def new_password_clicked(self, state):
        if state == QtCore.Qt.Checked:
            self.ui.new_password_edit.setEnabled(True)
            self.ui.change_password_button.setEnabled(True)
        else:
            self.ui.new_password_edit.setEnabled(False)
            self.ui.change_password_button.setEnabled(False)
