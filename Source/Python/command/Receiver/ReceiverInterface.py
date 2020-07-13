class Receiver:
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, state):
        if state in self._statedict.values():
            self._state = state

    @property
    def print(self):
        for state in self._statedict.keys():
            if self.state == self._statedict[state]:
                return state

    def __init__(self):
        self._statedict = dict({"turnoff" : 0, "turnon" : 1})
        self.state = self._statedict['turnoff']