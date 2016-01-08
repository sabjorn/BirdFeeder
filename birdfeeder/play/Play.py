import pyaudio
import wave
import sys

class Play:
    chunk = 1024

    def __init__(self, file):
        """ Init audio stream """ 
        self.wf = wave.open(file, 'rb')
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format = self.p.get_format_from_width(self.wf.getsampwidth()),
            channels = self.wf.getnchannels(),
            rate = self.wf.getframerate(),
            output = True,
            start = False, #this is necessary but was not in the pyaudio example code
            stream_callback=self.callback
        )

    def callback(self, in_data, frame_count, time_info, status):
        """ audio processing callback """
        #the ramp will go here somewhere
        data = self.wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

    def start(self):
        """ start playing stream """
        self.stream.start_stream()

    def stop(self):
        """ stop playing stream """
        self.stream.stop_stream()
        self.stream.close()
        self.wf.close()

    def close(self):
        """ Graceful shutdown """ 
        self.stream.close()
        self.p.terminate()
        self.wf.close()