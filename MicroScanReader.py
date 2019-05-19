import socket
import traceback

def most_frequent(List):
    return max(set(List), key = List.count)

class MicroScanReader(object):
    def __init__(self, ):
        self.client = None
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
        return True

    def close(self):
        try:
            self.client.close()
            self.client = None
        except:
            traceback.print_exc()

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
