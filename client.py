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
    # sock.connect((socket.gethostname(), 5555))
    sock.connect(("192.168.1.7", 1234))
    audio_data = sock.recv(4096)
    speaker.play_audio(audio_data)
    sock.close()
    # while True:
        # if ctr == 0:
        #     msg = sock.recv(1024)
        #     print(msg.decode("utf-8"))
        # audio_data = sock.recv(1024)
        # speaker.play_audio(audio_data)
        

if __name__=='__main__':
    Main()