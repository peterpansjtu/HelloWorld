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

    def _read(self):
        try:
            code = str(self.client.recv(4096), encoding='utf-8').split('\r\n')[0]
        except:
            print('read bar code failed, return ""')
            code = ''
        return code

    def run(self):
        while self.working == True:
            code = self._read()
            print(code)
            if (not code) or (code not in self.bar_code):
                self.bar_code = code

    def read(self):
        return self.bar_code
