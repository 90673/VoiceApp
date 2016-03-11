from Gui import *
from Client import *
from NetListener import *
from VoiceSocket import *
import time

listener = NetListener(1234)

c = gui()
c.updateclients(listener.getClients())

time.sleep(2)
if listener.getClients():
    v = VoiceSocket(listener.getClients()[0])
