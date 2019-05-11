# Echo client program
import re
import socket
import struct

# HOST = '192.168.200.50'    # The remote host
# PORT = 9600              # The same port as used by the server
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((HOST, PORT))

finsErrorsStrings = {
    0x0000000: None,
    0x0000001: 'The header is not FINS (ASCII code)',
    0x0000002: 'The data length is too long.',
    0x0000003: 'The command is not supported.',
    0x0000020: 'All connections are in use.',
    0x0000021: 'The specified node is already connected.',
    0x0000022: 'Attempt to access a protected node from an unspecified IP',
    0x0000023: 'The client FINS node address is out of range.',
    0x0000024: 'The same FINS node address is being used by the client and server.',
    0x0000025: 'All the node addresses available for allocation have been used.',
}

int2byte_dict = {0   : b'\x00\x00',
                 70  : b'\x00\x46',
                 100 : b'\x00\x64',
                 101 : b'\x00\x65',
                 200 : b'\x00\xc8',
                 201 : b'\x00\xc9',
                 203 : b'\x00\xcb',
                 }

def int_to_byte4(k):
    return k.to_bytes(4, byteorder='big')

def int_to_byte2(k):
    if k in int2byte_dict:
        return int2byte_dict[k]
    return k.to_bytes(2, byteorder='big')

def int_to_byte3(k):
    return k.to_bytes(3, byteorder='big')

def int_to_byte(k):
    return k.to_bytes(1, byteorder='big')

def binstr2int(s):
    #print('binstr2int', s)
    if type(s) == type('string'):
        s = bytes(s, encoding = "utf8")
    return int.from_bytes(s, 'big')
    n = 0
    for i in range(0, len(s)):
        n += ord(s[i]) * (1 << (8 * (len(s) - i - 1)))
    return n


def str2intlist(s):
    return [ord(c) for c in s]


def intlist_to_byte(l):
    return bytes(l)


def wordlist2str(wl):
    if wl[0] != 0xff:
        print('-- Neplatna')
        return ''
    cs = ''
    for d in wl[1:]:
        n1 = ((d >> 8) & 0xFF)
        n2 = (d & 0xFF)
        if n1 == 0:
            break
        if n2 == 0:
            cs += chr(n1)
            break
        cs += chr(n1) + chr(n2)
    return cs


def intlist2float(wdata):
    s = ""
    # danger to replace ! this reorder input word data - LSB is first string
    for v in wdata:
        s += chr(v & 0xFF)
        s += chr(v >> 8)
    # print repr(s)
    value = [None]
    if len(s) == 4:
        value = struct.unpack('f', s)
    if len(s) == 8:
        value = struct.unpack('d', s)
    return value[0]


class FinsTCPFrame():
    def __init__(self, cmdData=b'', rawFinsCmd=None, cmdFlags=None, DA1=None, SA1=None, MRC=None, SRC=None, command=0x02,
                 errorCode=0x00, serverAdr=0, clientAdr=0, rawTcpFrame=None):
        self.FINScommandFlags = ['ICF', 'RSV', 'GCT', 'DNA', 'DA1', 'DA2', 'SNA', 'SA1', 'SA2', 'SID', 'MRC', 'SRC',
                                 'data']
        if rawTcpFrame:
            self.fromRaw = True
            self.rawTcpFrame = rawTcpFrame
        else:
            self.fromRaw = False
            if (MRC or SRC or cmdData):
                # have some command data
                commandFlags = [
                    0x80,  # ICF
                    0x00,  # RSV 'RSV':0
                    0x02,  # 'GCT':0x02
                    0x00,  # 'DNA':0
                    serverAdr,  # 'DA1':0
                    0x00,  # 'DA2':0
                    0x00,  # 'SNA':0
                    clientAdr,  # 'SA1':0
                    0x00,  # 'SA2':0
                    0x00,  # 'SID':0
                    MRC,  # 'MRC':0
                    SRC,  # 'SRC':0
                ]
                if cmdFlags:
                    for k in cmdFlags.keys():
                        commandFlags[self.FINScommandFlags.index(k)] = cmdFlags[k]
                commandFrame = intlist_to_byte(commandFlags) + cmdData
            else:
                # frame have TCP header only or raw Fins Command Packet Provided
                if rawFinsCmd:
                    commandFrame = rawFinsCmd
                else:
                    commandFrame = ''
            self.rawTcpFrame = b'FINS'
            self.rawTcpFrame += int_to_byte4(8 + len(commandFrame))  # frame length
            self.rawTcpFrame += int_to_byte4(command)
            self.rawTcpFrame += int_to_byte4(errorCode)
            self.rawTcpFrame += commandFrame
    '''
    def make_frame(self):
        self.finsFrame = 'FINS'
        self.frameLength = 8 + len(self.finsCmdFrame)
        self.finsFrame += int_to_byte4(self.frameLength)
        self.finsFrame += int_to_byte4(self.finsCommand)
        self.finsFrame += int_to_byte4(self.finsErrorCode)
        self.finsFrame += self.finsCmdFrame
        return self.finsFrame
    '''
    @property
    def raw(self):
        return self.rawTcpFrame

    @property
    def disassembled(self):
        asm = {
            'header': binstr2int(self.rawTcpFrame[0: 4]),
            'length': binstr2int(self.rawTcpFrame[4: 8]),
            'command': binstr2int(self.rawTcpFrame[8:12]),
            'errCode': binstr2int(self.rawTcpFrame[12:16]),
        }
        if (asm['command'] == 2):
            asm['ICF'] = binstr2int(self.rawTcpFrame[16])
            asm['RSV'] = binstr2int(self.rawTcpFrame[17])
            asm['GCT'] = binstr2int(self.rawTcpFrame[18])
            asm['DNA'] = binstr2int(self.rawTcpFrame[19])
            asm['DA1'] = binstr2int(self.rawTcpFrame[20])
            asm['DA2'] = binstr2int(self.rawTcpFrame[21])
            asm['SNA'] = binstr2int(self.rawTcpFrame[22])
            asm['SA1'] = binstr2int(self.rawTcpFrame[23])
            asm['SA2'] = binstr2int(self.rawTcpFrame[24])
            asm['SID'] = binstr2int(self.rawTcpFrame[25])
            asm['MRC'] = binstr2int(self.rawTcpFrame[26])
            asm['SRC'] = binstr2int(self.rawTcpFrame[27])
            if self.fromRaw:
                # decode from response
                asm['MRES'] = binstr2int(self.rawTcpFrame[28])
                asm['SRES'] = binstr2int(self.rawTcpFrame[29])
                asm['response'] = self.rawTcpFrame[30:]
            else:
                asm['cmd'] = self.rawTcpFrame[28:]
        return asm

    @property
    def error(self):
        # return None if ok, else error string as string
        try:
            ec = binstr2int(self.rawTcpFrame[12:16])
            if ec == 0:
                ec = None
        except:
            ec = 'Error code not found' % self.finsErrorCode
        return ec

    @property
    def command(self):
        return binstr2int(self.rawTcpFrame[8:12])

    @property
    def commandResponse(self):
        return self.rawTcpFrame[30:]

    @property
    def finsData(self):
        """Return raw data after FINS TCP header"""
        return self.rawTcpFrame[16:]

    def __str__(self):
        asm = self.disassembled
        str = ''.join(["{0}:{1} ".format(k, asm[k], ) for k in asm.keys()])
        return str


class OmronPlcFinsTcp():
    def __init__(self, host, port):
        self.port = port
        self.host = host
        self.sock = None
        self.open = False
        self.clientNode = 0
        self.serverNode = 0
        self.sid = 0x04

    @property
    def _nextSid(self):
        return 0
        self.sid = (self.sid + 1) & 0xff
        return self.sid

    def openn(self):
        if self.open:
            # close if already open
            self.sock.close()
            self.open = False
        # open socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(5.0)
        try:
            self.sock.connect((self.host, self.port))
        except:
            return False
        # start establish fins communication
        #print('FINS cmd: request address')
        c1 = FinsTCPFrame(command=0, rawFinsCmd=int_to_byte4(0))
        #print("Sending: " + str(c1))
        self._send(c1.raw)
        r1raw = self._receive()
        r1 = FinsTCPFrame(rawTcpFrame=r1raw)
        #print("Received: " + str(r1))
        if r1.error:
            print('Error in address assign response: %s' % r1.error)
            try:
                print(' - this mean>%s' % finsErrorsStrings[r1.error])
            except:
                pass
            return False
        # set client and server address against response
        if r1.command != 1:
            print('Error bad response for address assign command: ' % r1.command)
            return False
        self.clientNode = binstr2int(r1.finsData[0:4])
        self.serverNode = binstr2int(r1.finsData[4:8])
        print('FINS address client: {0},server: {1}'.format(self.clientNode, self.serverNode, ))
        # Get PLC type as test dummy command
        #return self.doFinsCommand(MRC=0x05, SRC=0x01, cmdData='\x00')[0:20]
        return True

    def doFinsCommand(self, MRC, SRC, cmdData):
        # cmdData='',  rawFinsCmd = None,  cmdFlags = None,  DA1=None,  SA1=None,  MRC=None,  SRC=None,  command=0x02, errorCode=0x00, serverAdr = 0,  clientAdr = 0, rawTcpFrame=None ):
        c = FinsTCPFrame(MRC=MRC, SRC=SRC, cmdData=cmdData, serverAdr=self.serverNode, clientAdr=self.clientNode,
                         cmdFlags={'SID': self._nextSid})
        # print "Sending: " + str( c)
        self._send(c.raw)
        r_raw = self._receive()
        r = FinsTCPFrame(rawTcpFrame=r_raw)
        # print "Recieved: " + str( r)
        # print " disasm>" + str(r.disassembled)
        # TODO: check error and status..
        return r.commandResponse

    def close(self):
        self.sock.close()
        self.open = False

    def _send(self, raw):
        #print(raw)
        self.sock.send(raw)
        # print ' Send:' + repr(raw)

    def _receive(self):
        pr = self.sock.recv(8)
        length = binstr2int(pr[4:8])
        #print('received from plc: ', pr, length)
        r = pr + self.sock.recv(length)
        #print(r)
        # print ' Recv:' + repr(r)
        return r


class OmronPLC():
    def __init__(self):
        self.conType = None
        self.plcType = None
        '''
            'MemType':(bit, word)
        '''
        self.MEMCODES = {
            'C': (0x30, 0xB0),
            'W': (0x31, 0xB1),
            'H': (0x32, 0xB2),
            'A': (0x33, 0xB3),
            'D': (0x02, 0x82),
        }

    def openFins(self, address, port=9600):
        self.conType = 'FINS'
        self.conn = OmronPlcFinsTcp(address, port)
        self.plcType = self.conn.openn()
        return self.plcType

    def doRawFinsCommand(self, **kvarg):
        self.conn.doFinsCommand(kvarg)

    def close(self):
        if self.conType == 'FINS':
            self.conn.close()

    def readMemC(self, mem, length):
        memSpec = re.search(r'(.)([0-9]*):?([0-9]*)', mem).groups()
        (memCodeB, memCodeW) = self.MEMCODES[memSpec[0]]
        # construct mem specification form
        if memSpec[2]:
            # BIT specs
            memAdr = int_to_byte(memCodeB) + int_to_byte2(int(memSpec[1])) + int_to_byte(int(memSpec[2]))
        else:
            # Word Spec
            memAdr = int_to_byte(memCodeW) + int_to_byte2(int(memSpec[1])) + int_to_byte(0)
        rawres = self.conn.doFinsCommand(MRC=0x01, SRC=0x01,
                                         cmdData=memAdr + int_to_byte2(length))
        if memSpec[2]:
            # bit spec
            res = list(rawres)
        else:
            res = [binstr2int(rawres[i:i+2]) for i in range(0, len(rawres), 2)]
        return res

    def writeMemC(self, mem, wdata):
        memSpec = re.search('(.)([0-9]*):?([0-9]*)', mem).groups()
        (memCodeB, memCodeW) = self.MEMCODES[memSpec[0]]
        # construct mem specification form
        if memSpec[2]:
            # BIT specs
            memAdr = int_to_byte(memCodeB) + int_to_byte2(int(memSpec[1])) + int_to_byte(int(memSpec[2]))
        else:
            # Word Spec
            memAdr = int_to_byte(memCodeW) + int_to_byte2(int(memSpec[1])) + int_to_byte(0)
        rawdata = b''
        for d in wdata:
            rawdata += int_to_byte2(d)
        rawres = self.conn.doFinsCommand(MRC=0x01, SRC=0x02,
                                         cmdData=memAdr + int_to_byte2(len(wdata)) + rawdata)
        return rawres

    def set(self, address, bit):
        value = self.readMemC(address, 1)[0]
        value = value | 1 << bit
        self.writeMemC(address, [value])

    def clear(self, address, bit):
        value = self.readMemC(address, 1)[0]
        value = value & ~(1 << bit)
        self.writeMemC(address, [value])

    def read(self, address):
        return self.readMemC(address, 1)[0]

    def write(self, address, value):
        self.writeMemC(address, [value])


if __name__ == "__main__":
    plc = OmronPLC()
    plc.openFins('192.168.0.10', 9600)
    plc.set('C200', 0)
    print(plc.read('D100'))
    plc.write('D100', 100)
    plc.close()