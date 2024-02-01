# Used for taking and handling the client
import json


class Client():
    def __init__(self, client, role: str = "Driver"):
        self.client = client
        self.role = role


def client_authenticator(decoded_data):
  with open("clients.json", 'r') as json_file:
    clients = json.load(json_file)
    for client in clients.values():
      if client["VIN"] == decoded_data.split("::")[0] and client["SecretPassword"] == decoded_data.split("::")[1]:
        yield True, client, client["Role"]
  return False

if __name__ == "__main__":  # Debug to test authenticator
    b = client_authenticator("1::ExamplePassword")
    print(b)