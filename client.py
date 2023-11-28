import socket
import threading
import keyboard
import sys
import time
from Audio.audior import AudioRecord
from Audio.audiod import AudioPlayer 


def Main():
    speaker = AudioPlayer()
    mic = AudioRecord()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("192.168.1.46", 1234))

    try:
        audio_dat = b''
        while True:
            frames = mic.recordAudio()
            audiodata = mic.encodeFrames(frames)
            sock.send(audiodata)
            sock.sendall
            audio_data = sock.recv(65536)
            if not audio_data:
                break

            if audio_data == b'TERMINATE':
                print("Received termination signal from server")
                break

            audio_dat += audio_data

        # Play the accumulated audio data
        speaker.play_audio(audio_dat)

    except KeyboardInterrupt:
        print("Keyboard interrupt. Closing connection.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sock.close()


# def Main():
#     speaker = AudioPlayer()
#     mic = AudioRecord()
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.connect(("192.168.1.46", 1234))
    
#     try:
        
#         audio_dat=b''
#         while True:
#             frames = mic.recordAudio()
#             audiodata = mic.encodeFrames(frames)
#             sock.send(audiodata)

#             audio_data = sock.recv(65536)  # Adjust the buffer size as needed
#             if not audio_data:
#                 break  # Exit the loop if no more data is received
#             audio_dat+=audio_data
#         speaker.play_audio(audio_dat)
#         # print(type(audio_dat))
#         sock.send(audio_dat)
      
#     except Exception as e:
#         print(f"Error: {e}")
#     finally:
#         sock.close()
       

if __name__=='__main__':
    Main()