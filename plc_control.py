import socket

class plc_control(object):
    def __init__(self, ip, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((ip, port))

    def __del__(self):
        self.client.close()

    def set(self, addr, value):
        msg = b"set" + bytes([addr]) + bytes([value])
        self.client.send(msg)
        recv = self.client.recv(4096)

        return recv == b"ok"

    def get(self, addr):
        msg = b"get" + bytes([addr])
        self.client.send(msg)
        recv = self.client.recv(4096)
        print(recv)
        if recv[:2] == b"ok":
            return recv[2]
        return -1

if __name__ == '__main__':
    plc = plc_control('localhost', 12345)
    plc.set(1, 12)
    print(plc.get(1))