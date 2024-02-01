import socket

class Connection:
    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port
        self.sock = socket.socket(socket.AF_INET)

    def instate_connection(self):
        self.sock.connect((self.ip_address, self.port))
        self.sock.send("1::ExamplePassword") # Authentication