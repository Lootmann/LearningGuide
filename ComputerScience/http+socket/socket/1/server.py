import socket


def main():
    # AF_INET is IPv4 Network
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 8080))
    s.listen(5)

    while True:
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established!")
        clientsocket.send(bytes("Welcome to the server!", "utf-8"))
        clientsocket.close()


if __name__ == "__main__":
    main()
