import socket
import threading
import keyboard
import sys
import time
from Audio.audior import AudioRecord
from Audio.audiod import AudioPlayer

def Main():
    speaker = AudioPlayer()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("192.168.1.44", 1234))
    
    try:
        while True:
            audio_data = sock.recv(4096)  # Adjust the buffer size as needed
            if not audio_data:
                break  # Exit the loop if no more data is received
            speaker.play_audio(audio_data)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sock.close()

# def Main():
#     speaker = AudioPlayer()
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     # sock.connect((socket.gethostname(), 5555))
#     sock.connect(("192.168.1.44", 1234))
#     while True:
#         audio_data = sock.recv(496)
#         print(type(audio_data))
#         speaker.play_audio(audio_data)
#     sock.close()
#     # while True:
#         # if ctr == 0:
#         #     msg = sock.recv(1024)
#         #     print(msg.decode("utf-8"))
#         # audio_data = sock.recv(1024)
#         # speaker.play_audio(audio_data)
        

if __name__=='__main__':
    Main()