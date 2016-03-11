from tkinter import *
from threading import *
from Gui import *

class loginGui():
    def __init__(self):
        print("Login Gui")
        main1 = Thread(target=self.main)
        main1.start()

    def main(self):
        window = Tk()

        userbox = Entry(window)
        ipbox = Entry(window)
        portbox = Entry(window)
        connectbutton = Button(window,text="Connect",command = lambda: self.connect(window, userbox.get(), ipbox.get(), portbox.get()))

        userbox.pack()
        ipbox.pack()
        portbox.pack()
        connectbutton.pack()

        window.mainloop()

    def connect(self, window, name, ip, port):
        window.destroy()
        c = init(name,ip, port)


l = loginGui()