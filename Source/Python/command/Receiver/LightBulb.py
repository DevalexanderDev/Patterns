import sys, os

sys.path.append(os.path.abspath('../'))

from Receiver.ReceiverInterface import Receiver

class LightBulb(Receiver):
    def turnon(self):
        self.state = self._statedict['turnon']
        print("Ligth on")
    
    def undo(self):
        self.state = self._statedict['turnoff']
        print("Light off")