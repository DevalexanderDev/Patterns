import sys, os

sys.path.append(os.path.abspath('../'))

from Command.CommandInterface import Command

class Invoker:
    def __init__(self):
        self._commands = dict()

    def setCommand(self, buttonId, command:Command):
        self._commands[buttonId] = command

    def print(self):
        for command_key in self._commands:
            print("key - " + command_key + " " + self._commands[command_key].print())

    def executeCommand(self, buttonId):
        if buttonId in self._commands.keys():
            self._commands[buttonId].execute()
