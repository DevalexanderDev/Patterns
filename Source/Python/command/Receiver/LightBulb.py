import sys, os

sys.path.append(os.path.abspath('../'))

from Receiver.ReceiverInterface import Receiver

class LightBulb(Receiver):
    def __init__(self):
        self._statedict = dict({'turnoff' : 0, 'minimal' : 1, 'medium' : 2, 'high' : 3})
        self.state = self._statedict['turnoff']

    def toggle_light(self):
        state = self.state
        state_dict = self._statedict

        if state is state_dict['turnoff']:
            self.state = state_dict['minimal']

        elif state is state_dict['minimal']:
        	self.state = state_dict['medium']

        elif state is state_dict['medium']:
        	self.state = state_dict['high']

        elif state is state_dict['high']:
        	self.state = state_dict['turnoff']