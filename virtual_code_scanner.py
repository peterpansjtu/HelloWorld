import socket


class VirtualCodeScanner(object):
    def __init__(self, ip, port):
        self.__error = False
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client.connect((ip, int(port)))
        except:
            self.__error = True

    def __del__(self):
        self.client.close()

    def in_error(self):
        return self.__error

    def send(self, value):
        msg = b"code" + value.to_bytes(4, byteorder="little")
        try:
            self.client.send(msg)
            recv = self.client.recv(4096)
            return recv == b"ok"
        except:
            return False


if __name__ == '__main__':
    plc = VirtualCodeScanner('localhost', 12346)
    plc.send(0xffffffff)
