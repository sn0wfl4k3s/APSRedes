import socket

host = '127.0.0.1'
port = 12345

# instanciando o socket TCP para transmissão de dados em stream ↓
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ligando o socket a um endereço através do host e porta ↓
server.bind((host, port))
# colocando o socket em modo de escuta ↓
server.listen()
# informando que o servidor está disponível ↓
print('Servidor escutando...')
while True:
    # permitindo que o socket aceite conexões ↓
    conn, addr = server.accept()
    # recebendo o dado enviado pelo cliente ↓
    data = str(conn.recv(1024).decode())
    # verificando se o dado enviado é um número de ponto flutuante ↓
    if data.isdecimal():
        # calculando 25% desse valor e transformando em string ↓
        response = str(float(data) * 0.25)
        # enviando o valor calculado para o cliente ↓
        conn.send(response.encode())
        # informando o resultado e para quem foi enviado ↓
        print('{} enviado para: {}'.format(response, addr))
        # fechando a conexão com o cliente
        conn.close()
    else:
        # mensagem de erro caso o dado enviado não seja string decimal
        print('Erro: dado em formato não decimal.')
