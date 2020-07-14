import sys, os

sys.path.append(os.path.abspath('../'))

from Receiver.ReceiverInterface import Receiver

class Command:
    def __init__(self, receiver:Receiver):
        self._receiver = receiver
    
    def execute(self):
        self._receiver.execute()
        print(self.print() + ' ' + self._receiver.print)
    
    def undo(self):
        self._receiver.undo()
        print(self.print() + ' ' + self._receiver.print)

    def print(self):
    	return "Any command"