import socket

def convertSum(data): 
    num = data.split(" ")

    try:
        for i, x in enumerate(num): #Convert for int
            num[i] = int(x)

    except ValueError:
        data = "Only Interge!"
        return data

    return str(sum(num))

def main():
    host = 'localhost'
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))

    while True:
        try:
            print()
            s.listen()
            print("[*] Wait connection of client...")
            conn, ender = s.accept()
            print("[+] Connect in: ", ender)

            num_sum = []

            while True:
                data = conn.recv(1024)
                print(data)
                data = data.decode()

                #print(data, type(data), data.isnumeric())
                if data:
                    print("IF")

                    try:
                        num_sum.append(int(data))
                    except ValueError:
                        pass
                else:
                    print("ELSE")
                    conn.sendall(str.encode("AAA"))
                    print("Fechando conexão")
                    conn.close()
                    break
                print(num_sum)

        except ConnectionError:
            print("[-] Connection closed: ", ender)


main()