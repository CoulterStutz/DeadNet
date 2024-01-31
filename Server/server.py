# Program Name: Server.py
# Program Purpose: To host a server for the clients to connect to

import threading, socket
import API, Clients, Parser, Leaderboards
from termcolor import colored

def handle_client(client):

    auth_vin = client.recv(1024)
    dec_auth = auth_vin.decode('utf-8')

    if Clients.client_authenticator(dec_auth):
        None
    else:
        client.close()

    while True:
        try:
            d = client.recv(1024)
            if not d:
                break

            data = d.decode('utf-8')

        except Exception as E:
            print("Error Handling Client!")
            break

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 666))
    server.listen(5)
    print(f"[{colored('D3XDNET', 'red')}]: Listening on 0.0.0.0:666")

    while True:
        client, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


if __name__ == "__main__":
    start_server()