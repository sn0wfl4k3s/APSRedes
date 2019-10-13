import socket

host = '127.0.0.1'
port = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)
print('Server on...')
while True:
    sock, addr = server.accept()
    data = str(sock.recv(1024).decode())
    if data.isdecimal():
        response = str(float(data) * 0.25)
        sock.send(response.encode())
        print('{} sended for user {}'.format(response, addr))
    else:
        print('Data out of ideal format.. =/')