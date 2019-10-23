import socket

host = '127.0.0.1'
port = 12345

number = ''
while not number.isdecimal():
    number = input('Digite um número: ')
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.sendto(number.encode(), (host, port))
    data, addr = client.recvfrom(1024)
    result = float(data.decode())
    print('25% de {0} é {1:2}'.format(number, result))
    client.close()
except Exception as e:
    print('Um erro ocorreu ao durante a transmissão.')
