import sys, os

sys.path.append(os.path.abspath('../'))

from Receiver.ReceiverInterface import Receiver

class Teapot(Receiver):
    def execute(self):
        self.state = self._statedict['turnon']
    
    def undo(self):
        self.state = self._statedict['turnoff']