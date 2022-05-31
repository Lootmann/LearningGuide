import socket
import time


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 8080))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    length = 2**10
    msg = s.recv(length)
    print(msg.decode("utf-8"))


if __name__ == "__main__":
    while True:
        time.sleep(1)
        main()
