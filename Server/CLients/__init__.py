# Used for taking and handling the client

class Client():
  def __init__(self, client, vimIdentifier, hasRadarDetector:bool=False, role:str="Driver"):
    self.client = client
    self.vim = vimIdentifier
    self.hasRadarDetector = hasRadarDetector
    self.role = role