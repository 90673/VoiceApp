import socket
import pyaudio
import wave
import time

class VoiceSocket():
    def __init__(self, client):

        print("Streaming to client: ", client.name(), " At addresss: ", client.address())
        self.listen = 1
        frames=[]

        a = pyaudio.PyAudio()
        audiostream = a.open(format=a.get_format_from_width(2),channels=1,rate=44100,output=True,frames_per_buffer=1024)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("", 12345))
        s.listen(1)

        conn, addr = s.accept()
        i=1
        print("connected to :", addr)
        data = conn.recv(64)

        while data != '':
            audiostream.write(data)
            data = conn.recv(64)
            i=i+1
            frames.append(data)

        wf = wave.open("t.wav", 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(a.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b''.join(frames))
        wf.close()

