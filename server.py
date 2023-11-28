import socket
import threading
import keyboard
import sys
import time
from Audio.audior import AudioRecord
from Audio.audiod import AudioPlayer


def handle_client(client_socket):
    # Create an instance of the AudioRecord class
    mic = AudioRecord()
    speaker = AudioPlayer()
    audiodat = b''

    while True:
        dat = client_socket.recv(65536)
        print(type(dat))
        if not dat or dat == b'TERMINATE':
            break
        audiodat += dat

    if audiodat:
        speaker.play_audio(audiodat)

    # Record new audio
    frames = mic.recordAudio()
    audio_data = mic.encodeFrames(frames)
    client_socket.send(audio_data)

    client_socket.close()


# def handle_client(client_socket):
#     # Create an instance of the AudioRecord class
#     mic = AudioRecord()
#     speaker = AudioPlayer()
#     audiodat = b''
#     while True:
#         dat = client_socket.recv(65536)
#         print(type(dat))
#         if not dat:
#             break
#         audiodat+=dat
        
#     speaker.play_audio(audiodat)
#     # Record audio
#     frames = mic.recordAudio()
#     # Encode audio frames into a single binary data
#     audio_data = mic.encodeFrames(frames)
#     # print(audio_data)
#     # Send the audio data to the client
#     client_socket.send(audio_data)
    
#     client_socket.close()

def Main():
    IP = "192.168.1.46"
    PORT = 1234
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((IP, PORT))
    sock.listen(1)
    print(f"Server listening on port {PORT}")

    # stop_recording = threading.Event()

    try:
        while True:
            client_socket, address = sock.accept()
            print(f"Connection established with {address}")

            # Create a new thread for each client
            client_handler = threading.Thread(
                target=handle_client,
                args=(client_socket,),
            )
            client_handler.start()

    except KeyboardInterrupt:
        print("Server shutting down...")
        # stop_recording.set()
        client_socket.close()
        sock.close()

if __name__=='__main__':
    Main()
    # audR = AudioRecord()
    # frames = audR.recordAudio()
    # dat = audR.encodeFrames(frames)
    # # print(type(dat))
    # audD = AudioPlayer()
    # audD.play_audio(dat)