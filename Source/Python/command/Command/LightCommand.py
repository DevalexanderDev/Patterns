import sys, os

sys.path.append(os.path.abspath('../'))

from Command.CommandInterface import Command
from Receiver.ReceiverInterface import Receiver

class LightCommand(Command):
    def __init__(self, receiver:Receiver):
        self._receiver = receiver
        self._stackstate = list()
    
    def execute(self):
        self._stackstate.append(self._receiver.state)
        self._receiver.toggle_light()
        print(self.print() + ' ' + self._receiver.print)
    
    def undo(self):
        state = self._stackstate.pop()
        self._receiver.state = state
        print(self.print() + ' ' + self._receiver.print)

    def print(self):
        return "Light"
