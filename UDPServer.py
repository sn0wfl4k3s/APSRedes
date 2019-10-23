import socket

host = '127.0.0.1'
port = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((host, port))
print('Servidor escutando...')
while True:
    data, addr = server.recvfrom(1024)
    value = data.decode()
    if value.isdecimal():
        result = str(float(value) * 0.25)
        server.sendto(result.encode(), addr)
        print('{} enviado para {}'.format(result, addr))
    else:
        print('Dado em formato não decimal.. =/')
