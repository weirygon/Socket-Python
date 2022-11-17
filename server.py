import socket

host = 'localhost'
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()
print("Aguardando conexão de um cliente")
conn, ender = s.accept()
 
print("Conectado em: ", ender)

while True:
    data = conn.recv(1024)
    print(data, type(data))
    if "end" == data :
        print("Fechando conexão")
        conn.close()
        break
    conn.sendall(data)
