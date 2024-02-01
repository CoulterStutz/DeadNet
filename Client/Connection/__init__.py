# Import necessary modules
import socket
import time

class Connection:
    def __init__(self, ip_address, port):
        """
        Initialize the Connection class with the provided IP address and port.

        Parameters:
        - ip_address (str): The IP address of the server.
        - port (int): The port number for the connection.
        """
        self.ip_address = ip_address
        self.port = port
        self.sock = socket.socket(socket.AF_INET)
        self.message = {}

    def establish_connection(self):
        """
        Establish a connection to the server and perform authentication.

        Returns:
        None
        """
        # Connect to the server
        self.sock.connect((self.ip_address, self.port))

        # Authenticate with a predefined message
        auth_message = "1::ExamplePassword".encode('utf-8')
        self.sock.send(auth_message)

        # Enter data sending and receiving loop
        while True:
            # Your code to send data
            data_to_send = str(self.message)
            self.sock.send(data_to_send.encode('utf-8'))

            # Your code to receive data
            received_data = self.sock.recv(1024).decode('utf-8')
            print(f"Received data: {received_data}")

            time.sleep(1)  # Adjust as needed for your specific use case
