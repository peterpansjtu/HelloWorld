import socket
import threading
import time


class PLCControl(object):
    #signal = pyqtSignal(str, name='event')
    def __init__(self, config_file, ip, port = 9600):
        super(PLCControl, self).__init__()
        self.ip = ip
        self.port = port
        self.config_file = config_file
        self.poll_thread = threading.Thread(target=self.__poll)

    def __del__(self):
        #self.client.close()
        pass

    def __poll(self):
        '''
        track register's change to generate event
        event: start, stop, disconnect, warning
        '''
        while True:
            print(self.config_file)
            time.sleep(1)

    def start(self):
        self.poll_thread.start()

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
    plc = PLCControl('asd', '192.168.0.100', 2001)
    print('connect')
    # plc.set(1, 12)
    plc.start()
    print('asdfdsf')
