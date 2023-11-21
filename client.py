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
    sock.connect(("192.168.1.46", 1234))
    
    try:
        audio_data=b''
        while True:
            audio_data += sock.recv(65536)  # Adjust the buffer size as needed
            if not audio_data:
                speaker.play_audio(audio_data)
                break  # Exit the loop if no more data is received
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sock.close()
       

if __name__=='__main__':
    Main()