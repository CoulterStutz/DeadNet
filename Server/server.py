# Program Name: Server.py
# Program Purpose: To host a server for the clients to connect to

# Import necessary modules
import os
import threading
import socket
from pydub import AudioSegment
import io
from termcolor import colored
import API, Clients, Parser, Leaderboards

# Initialize instances
Transcribe = API.AWSTranscribe()
connected_clients = []

def encode_raw_mp3(raw_data):
    """
    Encode raw audio data to MP3 format.

    Parameters:
    - raw_data (bytes): Raw audio data.

    Returns:
    - bytes: Encoded MP3 data.
    """
    audio_segment = AudioSegment(
        raw_data,
        sample_width=2,  # Sample width in bytes (adjust as needed)
        channels=1,  # Number of audio channels (adjust as needed)
        frame_rate=44100  # Frame rate (adjust as needed)
    )

    # Export the audio segment as a raw MP3 data
    mp3_data = io.BytesIO()
    audio_segment.export(mp3_data, format="mp3")

    return mp3_data.getvalue()

def handle_client(client):
    """
    Handle the communication with a connected client.

    Parameters:
    - client (socket): Client socket.

    Returns:
    None
    """
    auth_vin = client.recv(1024)
    dec_auth = auth_vin.decode('utf-8')
    isAuthed, client_name, role = Clients.client_authenticator(dec_auth)

    if isAuthed:
        c = Clients.Client(client_name, role)
    else:
        client.close()

    while True:
        try:
            d = client.recv(1024)
            if not d:
                break

            data = d.decode('utf-8')
            client_speed = data[0]
            client_rpm = data[1]
            client_voice_data = [2]

            # Encode raw audio data to MP3
            mp3_data = encode_raw_mp3(client_voice_data)

            # Save encoded MP3 data to a temporary file
            with open(f"temp/encoding-{client_name}.mp3", "wb") as f:
                f.write(mp3_data)

            # Transcribe the MP3 file and parse the result
            TranscribeMessage = Transcribe.transcribe_message(client_name, f"temp/encoding-{client_name}.mp3")

            # Remove the temporary MP3 file
            os.remove(f"temp/encoding-{client_name}.mp3")

            # Parse the transcribed message
            ParsedMessage = Parser.parse_transcribe_output(TranscribeMessage)

        except Exception as E:
            print("Error Handling Client!")
            break

def start_server():
    """
    Start the server and handle incoming client connections.

    Parameters:
    None

    Returns:
    None
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 666))
    server.listen(5)
    print(f"[{colored('D3XDNET', 'red')}]: Listening on 0.0.0.0:666")

    while True:
        client, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

        # Create a new thread to handle the connected client
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
