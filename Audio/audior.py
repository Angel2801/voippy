import pyaudio
import wave
import keyboard
import threading
import base64

class AudioRecord:
    def __init__(self):
        self.CHUNK = 1024
        self.sample_format = pyaudio.paInt16
        self.channels = 1
        self.rate = 44100
        self.p = pyaudio.PyAudio()
        # self.save_file = "save.txt"
        self.recording = False
        
    def recordAudio(self):
        # info = self.p.get_host_api_info_by_index(0)
        # numdevices = info.get('deviceCount')
        # for i in range(0, numdevices):
        #      if (self.p.get_device_info_by_host_api_device_index(0, i).get('maxOutputChannels')) > 0:
        #          print("Input Device id ", i, " - ", self.p.get_device_info_by_host_api_device_index(0, i).get('name'))
        
        stream = self.p.open(
            format = self.sample_format, channels=self.channels,
            rate = self.rate, input=True, 
            frames_per_buffer = self.CHUNK
        )
        print("recording...")
        frames = []
        self.recording = True
        while self.recording:
            data = stream.read(self.CHUNK)
            frames.append(data)
            if keyboard.is_pressed("space"):
                stream.stop_stream()
                stream.close()
                self.p.terminate()
                self.recording = False
                return frames
            
    def encodeFrames(self, frames):
        audio_data = b''.join(frames)
        return audio_data