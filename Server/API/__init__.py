import boto3

class AWSTranscribe:
    def __init__(self):
        self.client = boto3.client("transcribe", region_name="us-west-2")

    def transcribe_message(self, sender_client, file):
        None
