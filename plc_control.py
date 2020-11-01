import socket
import threading


class PLCControl(QObject):
    signal = pyqtSignal(str, name='event')
    def __init__(self, config_file, ip, port = 9600):
        super(PLCControl, self).__init__()
        self.ip = ip
        self.port = port
        self.config_file = config_file
        self.poll_thread = threading.Thread(target=self.__poll)

    def __del__(self):
        self.client.close()

    def __poll(self):
        while True:
            print(self.config_file)

    def in_error(self):
        return self.__error

    def set(self, addr, value):
        msg = b"set" + bytes([addr]) + bytes([value])
        try:
            self.client.send(msg)
            recv = self.client.recv(4096)
            return recv == b"ok"
        except:
            return False

    def get(self, addr):
        self.client.settimeout(0.5)
        try:
            recv = self.client.recv(4096)
        except:
            self.client.settimeout(None)
            return None
        self.client.settimeout(None)
        return recv


if __name__ == '__main__':
    plc = PLCControl('192.168.0.100', 2001)
    print('connect')
    # plc.set(1, 12)
    print(plc.get(1))
