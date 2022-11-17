import socket

host = 'localhost'
port = 12345

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
except ConnectionError:
    print("[-] Error: Failed Connection!")
    exit()

print(f'{" SOMA ":=^50}')
print("Example=>1 2 3 4")
print("Soma = 10")
print("[*] Press Enter to exit")

while True:
    try:    
        string = input("=> ")
        
        if len(string) == 0:
            string = chr(0)
            s.sendall(str.encode((string)))
            break

        else:
            s.sendall(str.encode((string)))
            print("Soma =", (s.recv(1024)).decode())

    except KeyboardInterrupt:
        break
    except BrokenPipeError:
        print("[-] Error: Server Out!")
        break

print("[+] Finish!")
s.close()