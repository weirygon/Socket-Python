import socket

def convertSum(data): 
    num = data.split(" ")

    try:
        for i, x in enumerate(num): #Convert for int
            if x != '':
                num[i] = int(x)
            else:
                num[i] = 0

    except ValueError:
        data = "Only Interger!"
        return data

    return str(sum(num))

def main():
    host = 'localhost'
    port = 12345
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))

        while True:
            print()
            s.listen()
            print("[*] Wait connection of client...")
            conn, ender = s.accept()
            print("[+] Connect in: ", ender)

            try:

                while True:
                    data = conn.recv(1024)
                    data = data.decode()

                    if data != chr(0):
                        data = convertSum(data)
                        conn.sendall(str.encode(data))
                    
                    else:
                        print("[-] Connection closed:", ender)
                        conn.close()
                        break
            except ConnectionError:
                print("[-] Error: Connection Losted: ", ender)
                conn.close()

    except ConnectionError:
        print("[-] Error: Connection Losted: ", ender)
    except KeyboardInterrupt:
        print("[-] Exiting...")
        s.close()
    except OSError:
        print("[-] Error: Address already in use!")
    
    s.close()

main()