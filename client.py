import socket

host = '127.0.0.1'
port = 12345

numero = ''
while not numero.isdecimal():
    numero = input('Digite um número: ')
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    client.send(numero.encode())
    response = client.recv(1024)
