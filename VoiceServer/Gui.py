from tkinter import *
from threading import *
import time

class gui():
    def __init__(self):
        print("New gui created")

        self.clientlist = []

        maingui = Thread(target=self.main)
        maingui.start()

    def main(self):
        window = Tk()

        clientlister = Listbox(window)

        ref = Thread(target=self.refresh, args=(clientlister,))
        ref.start()

        clientlister.pack()

        window.mainloop()

    def getClients(self):
        return self.clientlist

    def addclient(self, name):
        self.clientlist.append(name)

    def updateclients(self, clients):
        self.clientlist = clients

    def refresh(self, clientlister):
        while 1:
            time.sleep(1)
            clientlister.delete(0, END)
            x = 0
            for i in self.clientlist:
                clientlister.insert(x, i.name())
                x = x + 1

    def clearclients(self):
        self.clientlist.clear()
