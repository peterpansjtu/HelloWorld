import socket
import logging


class PLCControl(object):
    def __init__(self, ip: str, port: int, logger=None):
        self.logger = logger or logging.getLogger(__name__)
        self.__error = False
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client.connect((ip, int(port)))
        except:
            self.logger.exception('Failed to connect to PLC ' + ip + ':' + str(port))
            self.__error = True

    def __del__(self):
        self.client.close()

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
        msg = b"get" + bytes([addr])
        try:
            self.client.send(msg)
            recv = self.client.recv(4096)
            if recv[:2] == b"ok":
                return recv[2]
        except:
            return -1


if __name__ == '__main__':
    plc = PLCControl('localhost', 12345)
    plc.set(1, 12)
    print(plc.get(1))
