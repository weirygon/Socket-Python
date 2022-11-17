import socket

host = 'localhost'
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))



while True:
    string = input("=> ")
    print(string)
    s.sendall(str.encode(string))
    data = s.recv(1024)

    if str == "end":
        break

print('Mensagem ecoada', data.decode())

