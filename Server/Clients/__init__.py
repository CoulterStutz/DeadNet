# Used for taking and handling the client
import json

class Client():
    """

    Attributes:
    - client (str): Client VIN.
    - role (str): Client role (default is "Driver").
    """
    def __init__(self, client, role: str = "Driver"):
        self.client = client
        self.role = role

def client_authenticator(decoded_data):
    """
    Authenticates a client based on decoded data.

    Parameters:
    - decoded_data (str): Decoded data containing client information.

    Returns:
    - tuple: Tuple containing authentication status, client object, and client role.
    """
    with open("clients.json", 'r') as json_file:
        clients = json.load(json_file)
        for client in clients.values():
            if client["VIN"] == decoded_data.split("::")[0] and client["SecretPassword"] == decoded_data.split("::")[1]:
                return True, Client(client["VIN"], client["Role"]), client["Role"]
    return False

if __name__ == "__main__":  # Debug to test authenticator
    b = client_authenticator("1::ExamplePassword")
    print(b)
