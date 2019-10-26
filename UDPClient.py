import socket

host = '127.0.0.1'
port = 12345

# declarando a variável de tipo string ↓
number = ''
# repetirá enquanto o número digitado não for decimal ↓
while not number.isdecimal():
    # lendo o número digitado pelo usuário ↓
    number = input('Digite um número: ')
try:
    # instanciando o socket UDP para transmissão de dados em stream ↓
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # enviando o número digitado pelo usuário para o servidor ↓
    client.sendto(number.encode(), (host, port))
    # recebendo a resposta do servidor ↓
    data, addr = client.recvfrom(1024)
    # convertendo o dado para float ↓
    result = float(data.decode())
    # printando na tela o resultado enviado pelo servidor ↓
    print('25% de {0} é {1:2}'.format(number, result))
    # fechando o socket cliente ↓
    client.close()
except:
    # alertando que ocorreu um erro ↓
    print('Ocorreu um erro durante a transmissão.')
