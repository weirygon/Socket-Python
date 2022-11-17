import socket

host = 'localhost'
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    try:    
        string = input("=> ")
        
        if len(string) == 0:
            print("IF")
            s.sendall(str.encode(chr(0)))
            break
        else:
            s.sendall(str.encode(str(string)))

    except KeyboardInterrupt:
        
        break

print("AAAAAAAAAAAAAAA")
print(s.recv(1024))

#print("Soma:", data)
print("[+] Finish!")
s.close()