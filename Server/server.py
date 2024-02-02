import socket
import os
from termcolor import colored


def handle_client(sock):
    authCode = sock.recv(1024).decode("utf-8")
    vin, pw = authCode.split("::")


def main(address, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((address, port))
    server.listen(5)

    print(f"[{colored('D3XDCOMMS', 'red')}]: Listening on port {colored(port), 'cyan'}")

    while True:
        client, addr = server.accept()
        print(f"[{colored('D3XDCOMMS', 'green')}]: Accepted New Connection From {colored(addr[0], 'cyan')}")

        # Start a new thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


if __name__ == "__main__":
    main()
