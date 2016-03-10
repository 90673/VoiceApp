from Gui import *
from Client import *
from NetListener import *
from VoiceSocket import *
import time

listener = NetListener(1234)

c = gui()
c.updateclients(listener.getClients())

time.sleep(2)

v = VoiceSocket(listener.getClients()[0])
