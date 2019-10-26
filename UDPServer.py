import socket

host = '127.0.0.1'
port = 12345

# instanciando o socket UDP para transmissão de dados em stream ↓
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# ligando o socket a um endereço através do host e porta ↓
server.bind((host, port))
# informando que o servidor está disponível para conexão↓
print('Servidor escutando...')
while True:
    # recebendo o dado e o endereço enviado pelo cliente ↓
    data, addr = server.recvfrom(1024)
    # transformando o dado de array de bytes para string ↓
    value = data.decode()
    # verificando se o dado enviado é um número de ponto flutuante ↓
    if value.isdecimal():
        # calculando 25% desse valor e transformando em string ↓
        result = str(float(value) * 0.25)
        # enviando o valor calculado para o cliente ↓
        server.sendto(result.encode(), addr)
        # informando o resultado e para qual endereço foi enviado ↓
        print('{} enviado para {}'.format(result, addr))
    else:
        # mensagem de erro caso o dado enviado não seja string decimal ↓
        print('Dado em formato não decimal.. =/')
