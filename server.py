import socket
import threading
import keyboard
import sys
import time
from Audio.audior import AudioRecord
from Audio.audiod import AudioPlayer


def Main():
    mic = AudioRecord()
    IP = "10.2.90.86"
    PORT = 1234
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.bind((socket.gethostname(), 5555))
    sock.bind((IP, PORT))
    sock.listen(5)
    print(f"Server listening on port {PORT}")
    ctr = 0
    
    while True:
        clientSocket, address = sock.accept()
        if ctr == 0:
            print(f"Connection established w/ {address}")
            clientSocket.send(bytes("Welcome to our SERVER!!", "utf-8"))
        frames = mic.recordAudio()
        dat = mic.encodeFrames(frames)
        clientSocket.send(dat)
        ctr+=1
        if keyboard.is_pressed('esc'):
            clientSocket.send(bytes("server shutting down", "utf-8"))
            sys.exit()
        

if __name__=='__main__':
    Main()
    # audR = AudioRecord()
    # frames = audR.recordAudio()
    # dat = audR.encodeFrames(frames)
    # # print(dat)
    # audD = AudioPlayer()
    # audD.play_audio(dat)