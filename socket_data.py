import socket

print('creating socket ...')
# Cria um objeto socket que utiliza o protocolo TCP devido ao parâmetro socket.SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket created')

# Estabelece uma conexão com o servidor através da porta 80
print('connection with remote host')
s.connect(('google.com',80))
print('connection ok')

# Envia uma mensagem ao servidor codificada em bytes
s.send(b'GET /index.html HTML/1.1\r\n\r\n')
while 1:
    # Recebe uma resposta do servidor que é decodificada para futura visualização
    data = s.recv(2048).decode()  
    print(data)
    if data == '':
        break
print('closing the socket')

# Fecha o socket interrompendo a comunicação com o servidor
s.close()