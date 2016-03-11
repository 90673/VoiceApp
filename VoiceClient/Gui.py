import tkinter
from threading import *
from NetInit import *

class gui():
    def __init__(self):
        print("Gui created")


class init():
    def __init__(self, name, ip, port):
        print("Connecting to", ip, ":", port)
        c = netInit(name, ip, port)

