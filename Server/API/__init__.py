# Import necessary module
import boto3

class AWSTranscribe:
    def __init__(self):
        """
        Initialize the AWSTranscribe class with AWS Transcribe and S3 clients.

        Parameters:
        None
        """
        self.transcribe_client = boto3.client("transcribe", region_name="us-west-2")
        self.s3_client = boto3.client("s3", region_name="us-west-2")
        self.bucket_name = "your-s3-bucket-name"  # Replace with your actual S3 bucket name

    def transcribe_message(self, sender_client, file_path):
        """
        Transcribe an audio file stored in an S3 bucket.

        Parameters:
        - sender_client (str): Sender client identifier.
        - file_path (str): Path to the audio file.

        Returns:
        - str: Transcribed text.
        """
        # Upload the file to S3
        object_key = f"{sender_client}/{file_path}"  # Customize the object key as needed
        self.s3_client.upload_file(file_path, self.bucket_name, object_key)

        # Start transcription job
        job_name = f"transcription-{sender_client}"
        job_response = self.transcribe_client.start_transcription_job(
            TranscriptionJobName=job_name,
            LanguageCode="en-US",
            MediaFormat="mp3",
            Media={
                "MediaFileUri": f"s3://{self.bucket_name}/{object_key}"
            }
        )

        # Wait for transcription job to complete
        self.transcribe_client.get_waiter("transcription_job_completed").wait(
            TranscriptionJobName=job_name
        )

        # Get transcription results
        result_uri = job_response["TranscriptionJob"]["Transcript"]["TranscriptFileUri"]
        transcription_result = self.s3_client.get_object(Bucket=self.bucket_name, Key=result_uri[len(f"s3://{self.bucket_name}/"):])
        transcribed_text = transcription_result["Body"].read().decode("utf-8")

        # Delete the S3 objects and transcription job if needed
        self.s3_client.delete_object(Bucket=self.bucket_name, Key=object_key)
        self.transcribe_client.delete_transcription_job(TranscriptionJobName=job_name)

        return transcribed_text

# Example usage:
# transcribe_instance = AWSTranscribe()
# result = transcribe_instance.transcribe_message("client123", "path/to/your/file.mp3")
# print(result)
