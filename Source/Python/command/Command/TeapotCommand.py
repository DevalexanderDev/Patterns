import sys, os

sys.path.append(os.path.abspath('../'))

from Command.CommandInterface import Command

class TeapotCommand(Command):
    def print(self):
        return "Teapot"