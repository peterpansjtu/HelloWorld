import socket


class MicroScanReader(object):
    def __init__(self,):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __del__(self):
        self.client.close()

    def open(self, ip, port):
        try:
            self.client.settimeout(5.0)
            self.client.connect((ip, int(port)))
        except:
            print('MicroScan connect failed')
            return False
        return True

    def read(self):
        self.client.settimeout(0.5)
        try:
            recv = self.client.recv(4096)
        except:
            self.client.settimeout(None)
            return b''
        self.client.settimeout(None)
        return recv
