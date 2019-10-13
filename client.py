import socket

host = '127.0.0.1'
port = 12345

number = ''
while not number.isdecimal():
    number = input('Digite um número: ')
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    client.send(number.encode())
    result = float(client.recv(1024))
    print('25% de {0} é {1:2}'.format(number, result))
except:
    print('Um erro ocorreu ao tentar conectar-se')