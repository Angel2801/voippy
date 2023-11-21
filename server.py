import socket
import threading
import keyboard
import sys
import time
from Audio.audior import AudioRecord
from Audio.audiod import AudioPlayer

def handle_client(client_socket, stop_event):
    mic = AudioRecord()
    speaker = AudioPlayer()

    try:
        while not stop_event.is_set():
            # Record new audio data
            frames = mic.recordAudio()
            # Encode audio frames into a single binary data
            audio_data = mic.encodeFrames(frames)
            # Send the new audio data to the client
            client_socket.send(audio_data)
            audio_data_recv = b''
            while True:
                audio_data_recv += client_socket.recv(65536)  # Adjust the buffer size as needed
                if not audio_data:
                    speaker.play_audio(audio_data_recv)
                    break  # Exit the loop if no more data is received
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

# def handle_client(client_socket):
#     # Create an instance of the AudioRecord class
#     mic = AudioRecord()

#     # Record audio
#     frames = mic.recordAudio()

#     # Encode audio frames into a single binary data
#     audio_data = mic.encodeFrames(frames)
    
#     # print(audio_data)

#     # Send the audio data to the client
#     client_socket.send(audio_data)

#     # Close the client socket
#     client_socket.close()

def Main():
    IP = "192.168.1.46"
    PORT = 1234
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((IP, PORT))
    sock.listen(1)
    print(f"Server listening on port {PORT}")

    stop_recording = threading.Event()

    try:
        while True:
            client_socket, address = sock.accept()
            print(f"Connection established with {address}")

            # Create a new thread for each client
            client_handler = threading.Thread(
                target=handle_client,
                args=(client_socket, stop_recording),
            )
            client_handler.start()

    except KeyboardInterrupt:
        print("Server shutting down...")
        stop_recording.set()
        sock.close()


# def Main():
#     mic = AudioRecord()
#     IP = "192.168.1.46"
#     PORT = 1234
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.bind((IP, PORT))
#     sock.listen(1)
#     print(f"Server listening on port {PORT}")

#     stop_recording = threading.Event()

#     try:
#         while True:
#             client_socket, address = sock.accept()
#             print(f"Connection established with {address}")

#             # Create a new thread for each client
#             client_handler = threading.Thread(
#                 target=handle_client,
#                 args=(client_socket,),
#             )
#             client_handler.start()

#     except KeyboardInterrupt:
#         print("Server shutting down...")
#         stop_recording.set()
#         sock.close()

if __name__=='__main__':
    Main()
    # audR = AudioRecord()
    # frames = audR.recordAudio()
    # dat = audR.encodeFrames(frames)
    # print(type(dat))
    # audD = AudioPlayer()
    # audD.play_audio(dat)