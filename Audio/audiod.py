import pyaudio
import base64

class AudioPlayer:
    def __init__(self):
        self.CHUNK = 1024
        self.sample_format = pyaudio.paInt16
        self.channels = 1
        self.rate = 44100
        self.p = pyaudio.PyAudio()
        # self.save_file = "save.txt"
        self.recording = False

    def play_audio(self, audio_data):
        stream = self.p.open(
            format=self.sample_format,
            channels=self.channels,
            rate=self.rate,
            output=True,
        )
        stream.write(audio_data)
        stream.stop_stream()
        stream.close()