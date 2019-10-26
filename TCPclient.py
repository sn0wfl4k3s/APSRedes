import socket

host = '127.0.0.1'
port = 12345

# setando a mensagem de entrada ↓
inputMessage = 'Digite um número: '
# lendo o número digitado ↓
number = input(inputMessage)
# repetirá enquanto o número digitado não for decimal ↓
while not number.isdecimal():
    # mensagem de erro caso digite um valor inválido ↓
    print('Valor inválido, por favor ', end='')
    # solicitando o número novamente ↓
    number = input(inputMessage.lower())
try:
    # instanciando o socket TCP para transmissão de dados em stream ↓
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # conectando ao endereço do servidor ↓
    client.connect((host, port))
    # enviando o número digitado pelo usuário para o servidor ↓
    client.send(number.encode())
    # recebendo a resposta do servidor ↓
    result = float(client.recv(1024))
    # fechando a conexão com o servidor ↓
    client.close()
    # printando na tela o resultado enviado pelo servidor ↓
    print('25% de {0} é {1:2}'.format(number, result))
except:
    # alertando que ocorreu um erro ↓
    print('Ocorreu um erro durante a transmissão.')
