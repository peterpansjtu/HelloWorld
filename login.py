from PyQt5 import QtWidgets
from hashlib import md5
import os

import ui_login

class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.ui = ui_login.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.login_button.clicked.connect(self.handleLogin)

    def handleLogin(self):
        username_in = self.ui.username_edit.text()
        password_in = self.ui.password_edit.text()
        username_in = md5(username_in.encode()).hexdigest()
        password_in = md5(password_in.encode()).hexdigest()
        username = md5('admin'.encode()).hexdigest()
        password = md5('admin'.encode()).hexdigest()
        if os.path.isfile('密码.txt'):
            with open('密码.txt', 'r', encoding='utf8') as f:
                lines = f.read().splitlines()
                if len(lines) == 2:
                    [username, password] = lines
        if (username_in == username and password_in == password):
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Error', '用户名或密码不正确')
