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
    # alertando que ocorreu um erro durante a comunicação com o servidpr ↓
    print('Um erro ocorreu ao tentar conectar-se')
