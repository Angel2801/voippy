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

    # Record audio
    frames = mic.recordAudio()

    # Encode audio frames into a single binary data
    audio_data = mic.encodeFrames(frames)

    # Send the audio data to the client
    client_socket.send(audio_data)

    # Close the client socket
    client_socket.close()

def Main():
    mic = AudioRecord()
    # IP = "10.2.90.86"
    IP = "192.168.1.7"
    PORT = 1234
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.bind((socket.gethostname(), 5555))
    sock.bind((IP, PORT))
    sock.listen(1)
    print(f"Server listening on port {PORT}")
    
    while True:
        client_socket, address = sock.accept()
        print(f"Connection established with {address}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()
        
    # ctr = 0
    
    # while True:
    #     clientSocket, address = sock.accept()
    #     if ctr == 0:
    #         print(f"Connection established w/ {address}")
    #         clientSocket.send(bytes("Welcome to our SERVER!!", "utf-8"))
    #     # frames = mic.recordAudio()
    #     # dat = mic.encodeFrames(frames)
        
    #     # clientSocket.send(dat)
    #     ctr+=1
    #     if keyboard.is_pressed('esc'):
    #         clientSocket.send(bytes("server shutting down", "utf-8"))
    #         sock.close()
    #         sys.exit()
        

if __name__=='__main__':
    Main()
    # audR = AudioRecord()
    # frames = audR.recordAudio()
    # dat = audR.encodeFrames(frames)
    # # print(dat)
    # audD = AudioPlayer()
    # audD.play_audio(dat)