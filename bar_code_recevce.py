import socket

from PyQt5.QtCore import QThread, pyqtSignal


class BarCodeReceiveThread(QThread):
    """docstring for BarCodeReceive"""
    signal = pyqtSignal(str, name='new_bar_code')

    def __init__(self, ip, port, bufsize=4096):
        super(BarCodeReceiveThread, self).__init__()
        self.ip = ip
        self.port = port
        self.bufsize = bufsize
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((ip, port))
        self.s.listen(5)

    def run(self):
        while True:
            conn, addr = self.s.accept()
            print(addr, "connected")
            while True:
                data = conn.recv(self.bufsize)
                if not data:
                    break
                opcode = data[:4]
                if opcode == b"code":
                    bar_code = int.from_bytes(data[4:], byteorder='little')
                    print(int.from_bytes(data[4:], byteorder='little'))
                    self.signal.emit(str(bar_code))
                    conn.send(b"ok")
                else:
                    print("Invalid data from", addr)
            conn.close()
            print(addr, "disconnected")
