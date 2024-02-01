import socket

class Connection:
    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port
        self.sock = socket.socket(socket.AF_INET)
        self.transmission_message = {1:None,2:None,3:None}

    def establish_connection(self):
        self.sock.connect((self.ip_address, self.port))
        auth_message = "1::ExamplePassword".encode('utf-8')  # Authentication message should be encoded
        self.sock.send(auth_message)
