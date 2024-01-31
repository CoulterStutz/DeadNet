# Used for taking and handling the client
import json


class Client():
    def __init__(self, client, vimIdentifier, hasRadarDetector: bool = False, role: str = "Driver"):
        self.client = client
        self.vim = vimIdentifier
        self.hasRadarDetector = hasRadarDetector
        self.role = role


def ClientAuthenticator(decodedData):
    with open("clients.json", 'r') as j:
        c = j.read()
        clients = eval(c)


if __name__ == "__main__":
    ClientAuthenticator("1")
