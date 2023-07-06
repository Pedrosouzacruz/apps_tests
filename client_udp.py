import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Cliente socket criado com sucesso")

host = "localhost"
porta = 5433

message = "Ola servidor firmeza?"

try:
    print(f"Cliente: {message}")
    s.sendto(message.encode(), (host,5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print(f"Cliente: {dados}")
finally:
    print("Fechando a conexão")
    s.close()