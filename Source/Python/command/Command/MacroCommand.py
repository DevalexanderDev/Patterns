import sys, os

sys.path.append(os.path.abspath('../'))

from Command.CommandInterface import Command
from Receiver.ReceiverInterface import Receiver

class MacroCommand(Command):
	def __init__(self, listCommand):
		self._commands = list()
		for command in listCommand:
			self._commands.append(command)

	def execute(self):
		for command in self._commands:
			command.execute()

	def undo(self):
		for command in self._commands:
			command.undo()

	def print(self):
		str = ''
		for command in self._commands:
			str += command.print() + ' '
		return str