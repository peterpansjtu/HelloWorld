import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('localhost', 12345))
serv.listen(5)
registers = {1: 0}

while True:
    conn, addr = serv.accept()
    print(addr, "connected")
    while True:
        for k in registers:
            registers[k] += 1
        print(registers)
        data = conn.recv(4096)
        if not data:
            break
        opcode = data[:3]
        if opcode == b"set":
            print(data[4])
            registers[data[3]] = data[4]
            conn.send(b"ok")
        elif opcode == b"get":
            conn.send(b"ok" + bytes([registers[data[3]]]))
    conn.close()
    print('client disconnected')
