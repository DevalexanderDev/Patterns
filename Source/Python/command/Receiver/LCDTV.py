import sys, os

sys.path.append(os.path.abspath('../'))

from Receiver.ReceiverInterface import Receiver

class LCDTV(Receiver):
    def change_channel(self):
        print("Изменил канал")

    def execute(self):
        self.state = self._statedict['turnon']
        print("TV on")
    
    def undo(self):
        self.state = self._statedict['turnoff']
        print("TV off")