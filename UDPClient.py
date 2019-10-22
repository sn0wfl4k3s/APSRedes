import socket

host = '0.0.0.0'
port = 12000

number = ''
while not number.isdecimal:
  number = input('Digite um número: ')

try:
  client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  client.sendto(number, (host, port))
  result, addr = client.recvfrom(2048)
  client.close()
  print('25% de {0} é {1:2}'.format(number, result))
except:
  print('Um erro ocorreu ao tentar conectar-se')
