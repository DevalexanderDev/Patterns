import sys, os

sys.path.append(os.path.abspath('../'))

from Command.CommandInterface import Command

class TVCommand(Command):
    def print(self):
        return "Tv"