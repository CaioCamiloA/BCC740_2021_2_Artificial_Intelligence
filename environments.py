import numpy as np


class ToilletPaperEnv():

    def __init__(self, price,
                 tpnumber, max_capacity) -> None:

        self.price = 2
        self.TPNumber = tpnumber
        self.max_capacity = max_capacity
        self.clock = 0

    def initial_percepts(self) -> dict[float, int, int]:

        percepts = {'price': self.price,
                    'tpnumber': self.TPNumber,
                    'max_capacity': self.max_capacity}

        return percepts

    def change_state(self, action) -> dict[float, int, int]:

        self.TPNumber += action['to_buy']

        usage = min(np.random.randn()*100, self.TPNumber)

        self.TPNumber -= usage if usage > 0 else 0

        self.price = max(self.price + np.random.randn() * 0.1, 0.5)

        percepts = {'price': self.price,
                    'tpnumber': self.TPNumber,
                    'max_capacity': self.max_capacity}

        self.clock += 1

        return percepts
