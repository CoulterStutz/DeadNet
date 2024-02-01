import socket
import time


class Connection:
    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port
        self.sock = socket.socket(socket.AF_INET)

    def establish_connection(self):
        self.sock.connect((self.ip_address, self.port))
        auth_message = "1::ExamplePassword".encode('utf-8')
        self.sock.send(auth_message)

        while True:
            # Your code to send data
            data_to_send = input("Enter data to send: ")
            self.sock.send(data_to_send.encode('utf-8'))

            # Your code to receive data
            received_data = self.sock.recv(1024).decode('utf-8')
            print(f"Received data: {received_data}")

            time.sleep(1)  # Adjust as needed for your specific use case
