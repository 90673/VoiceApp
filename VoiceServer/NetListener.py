import socket
from threading import *
import time
from Client import *

class NetListener():
    def __init__(self, port):
        self.clients = []

        print("Listening on: ", port)
        self.listen = True

        self.listensocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.listensocket.bind(("", port))

        self.mainlistener = Thread(target=self.Listen, args=(self.listensocket, port,))
        self.mainlistener.start()


    def Listen(self,socket, port):
        while self.listen:
            message, address = socket.recvfrom(1024)
            print(message.decode())

            if message.decode().rstrip().split(',')[0] == "LOGIN":
                print("Login request from user: ", message.decode().rstrip().split(',')[1])
                self.newclient(0, address, message.decode().rstrip().split(',')[1] )

    def stop(self):
        self.listen = False
        print("Stopped listening")

    def open(self):
        self.listen = True
        print("Started listening")

    def getClients(self):

        return self.clients

    def newclient(self, id, addr, name):
        c = client(id, addr, name)
        self.clients.append(c)


