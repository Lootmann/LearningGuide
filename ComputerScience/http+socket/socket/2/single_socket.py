import socket


def main():
    # create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # server_socket.bind((socket.gethostname(), 8080))
    server_socket.bind(("localhost", 8080))

    # 接続要求の最大値
    server_socket.listen(5)

    # main loop
    while True:
        client_socket, (address, port) = server_socket.accept()
        print(f"New Client: {client_socket}: {address}:{port}")

        while True:
            try:
                msg = client_socket.recv(1024)
                print(f"Recv: {msg}")
            except OSError:
                break

            if len(msg) == 0:
                break

            # echo
            sent_message: bytes = msg

            while True:
                sent_length = client_socket.send(sent_message)
                if sent_length == len(sent_message):
                    break
                else:
                    sent_message = sent_message[sent_length:]

            print(f"Send: {sent_message}")

        client_socket.close()
        print(f"Closed ... : {client_socket}: {address}:{port}")


if __name__ == "__main__":
    main()
