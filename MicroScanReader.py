import socket
import traceback

from PyQt5.QtCore import QThread


class MicroScanReader(QThread):
    def __init__(self, ):
        super(MicroScanReader, self).__init__()
        self.client = None
        self.bar_code = ''
        self.working = False
        return

    def __del__(self):
        try:
            self.client.close()
        except:
            pass

    def open(self, ip, port):
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.settimeout(5.0)
            self.client.connect((ip, int(port)))
        except Exception as e:
            print('MicroScan connect failed')
            traceback.print_exc()
            return False
        self.working = True
        self.client.settimeout(1.0)
        self.start()
        return True

    def close(self):
        try:
            self.working = False
            self.wait()
            self.client.close()
            self.client = None
            self.bar_code = ''
        except:
            traceback.print_exc()

    def two_equal_code(self, string):
        if len(string) % 2:
            return False
        sub_len = int(len(string) / 2)
        if string[:sub_len] == string[sub_len:]:
            return True
        return False

    def _read(self):
        try:
            trial = 1
            code = ''
            while True:
                if trial >= 10:
                    break
                part = str(self.client.recv(4096), encoding='utf-8').replace("\r\n", "").replace("\n", "").replace("\r", "")
                print("Mirco Scanner read: ", part)
                code += part
                if self.two_equal_code(code):
                    code = code[:int(len(code) / 2)]
                    print("Mirco Scanner bar code: ", code)
                    break
                trial += 1
        except:
            print('read bar code failed, return ""')
            code = ''
        return code

    def run(self):
        while self.working is True:
            code = self._read()
            code.replace("\r\n", "")
            code.replace("\r", "")
            code.replace("\n", "")
            self.bar_code = code
            print("self.bar_code = ", self.bar_code)

    def read(self):
        return self.bar_code
