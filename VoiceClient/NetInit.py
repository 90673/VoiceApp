import socket
from threading import *

class netInit():
    def __init__(self, name, ip, port):
        print("Sending request to:",ip,":", port)
        connect = Thread(target=self.connect, args=(name, ip, port,))
        connect.start()

    def connect(self, name, ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
        s.connect((ip, int(port)))
        s.send("LOGIN,SAM".encode())
        s.close()
        print("Request sent")