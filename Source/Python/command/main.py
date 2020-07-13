from Command.LightCommand import LightCommand
from Command.TeapotCommand import TeapotCommand
from Command.TVCommand import TVCommand
from Receiver.LCDTV import LCDTV
from Receiver.Teapot import Teapot
from Receiver.LightBulb import LightBulb
from Invoker.Invoker import Invoker

teapot = TeapotCommand(Teapot())
tv = TVCommand(LCDTV())
light = LightCommand(LightBulb())

controlPanel = Invoker()
controlPanel.setCommand("1", teapot)
controlPanel.setCommand("2", tv)
controlPanel.setCommand("3", light)

s = ''

while s != 'n':
    controlPanel.executeCommand(s)

    controlPanel.print()
    s = input("Ваш выбор ")
