"""PyAudio example: Record a few seconds of audio and save to a WAVE file."""
import pyaudio
import wave
import speech_recognition as sr


class Speech2txt:
    def __init__(self):
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.RECORD_SECONDS = 5
        self.WAVE_OUTPUT_FILENAME = "output.wav"

    def Sp2txt(self):
        p = pyaudio.PyAudio()
        stream = p.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)
        print("* recording")
        frames = []
        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = stream.read(self.CHUNK)
            frames.append(data)
        print("* done recording")
        stream.stop_stream()
        stream.close()
        p.terminate()
        wf = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        # initialize the recognizer
        r = sr.Recognizer()
        # open the file
        with sr.AudioFile(self.WAVE_OUTPUT_FILENAME) as source:
            # listen for the data (load audio to memory)
            audio_data = r.record(source)
            # recognize (convert from speech to text)
            self.Langtxt = r.recognize_google(audio_data)
            print(self.Langtxt)
            return self.Langtxt
