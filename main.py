import threading, socket
import API, Clients, Parser, Leaderboards
from termcolor import colored

def handle_client(client):
    None

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
