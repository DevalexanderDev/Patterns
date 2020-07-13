import sys, os

sys.path.append(os.path.abspath('../'))

from Receiver.ReceiverInterface import Receiver


class Command:
    def __init__(self, receiver:Receiver):
        self._receiver = receiver
    
    def execute(self):
        self._receiver.execute()
    
    def undo(self):
        self._receiver.undo()