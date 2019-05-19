import socket

def most_frequent(List):
    return max(set(List), key = List.count)

class MicroScanReader(object):
    def __init__(self, ):
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
        recv = []
        self.client.settimeout(2)
        try:
            for i in range(0, 3):
                code = str(self.client.recv(4096), encoding='utf-8').split('\r\n')
                for c in code:
                    recv.append(c)
        except:
            self.client.settimeout(None)
            recv.append('')
        self.client.settimeout(None)
        return most_frequent(recv)
