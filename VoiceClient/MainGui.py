import socket
import pyaudio
import wave

#record
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 40

HOST = '192.168.0.2'    # The remote host
PORT = 1234              # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

# connect the socket, think of it as connecting the cable to the address location
s.connect((HOST, PORT))

# send the command
s.send("LOGIN,SAM".encode())

# close the socket
s.close()

PORT = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)


print("*recording")

frames = []

for i in range(0, int(RATE/CHUNK*9999999999999999999999)):
 data  = stream.read(CHUNK)
 frames.append(data)
 s.sendall(data)

print("*done recording")

stream.stop_stream()
stream.close()
p.terminate()
s.close()

print("*closed")