"""
 Implements a simple HTTP/1.0 Server
"""

import socket


# Define socket host and port
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8000


def main():
    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(1)

    print("Listening on port %s ..." % SERVER_PORT)
    print("URL is http://localhost:%s" % SERVER_PORT)

    while True:
        # Wait for client connections
        client_connection, _ = server_socket.accept()

        # Get the client request
        request = client_connection.recv(1024).decode()
        print(request)

        # Parse HTTP headers
        headers = request.split("\n")

        # header
        # GET /ipsum.html HTTP/1.0
        filename = headers[0].split()[1]

        if filename == "/":
            filename = "/index.html"

        if filename == "/favicon.ico":
            continue

        try:
            fin = open("htdocs" + filename)
            content = fin.read()
            fin.close()
            response = "HTTP/1.0 200 OK\n\n" + content

        except FileNotFoundError:
            response = "HTTP/1.0 404 NOT FOUND\n\nFile Not Found"

        client_connection.sendall(response.encode())
        client_connection.close()

    # Close socket
    server_socket.close()


if __name__ == "__main__":
    main()
