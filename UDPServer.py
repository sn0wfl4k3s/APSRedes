import socket

host = ''
port = 12000

try:
  server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  server.bind((host, port))
  print('Servidor escutando...')
  while True:
    data, addr = server.recvfrom(2048)
    if str(data).isdecimal():
      response = str(float(data) * 0.25)
      server.sendto(response, addr)
    else:
      print('Dado em formato não decimal.. =/')
except:
  print('ocorreu um erro')
