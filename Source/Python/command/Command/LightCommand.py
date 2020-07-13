import sys, os

sys.path.append(os.path.abspath('../'))

from Command.CommandInterface import Command

class LightCommand(Command):
    def print(self):
        return "Light"