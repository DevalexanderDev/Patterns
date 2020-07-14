from Command.LightCommand import LightCommand
from Command.TeapotCommand import TeapotCommand
from Command.TVCommand import TVCommand
from Command.MacroCommand import MacroCommand
from Receiver.LCDTV import LCDTV
from Receiver.Teapot import Teapot
from Receiver.LightBulb import LightBulb
from Invoker.Invoker import Invoker

teapot = TeapotCommand(Teapot())
tv = TVCommand(LCDTV())
light = LightCommand(LightBulb())

macro = MacroCommand([tv, teapot])

controlPanel = Invoker()
controlPanel.setCommand("1", teapot)
controlPanel.setCommand("2", tv)
controlPanel.setCommand("3", light)
controlPanel.setCommand("4", macro)

s = ''

while s != 'n':
    controlPanel.executeCommand(s)
    controlPanel.undoCommand(s)

    controlPanel.print()
    s = input("Ваш выбор ")
