class ToilletPaperAg():

    def __init__(self, env) -> None:
        self.env = env
        self.price_average = 0
        self.current_percepts = env.initial_percepts()
        self.usage_average = self.current_percepts['tpnumber']
        self.price_average = self.current_percepts['price']
        self.price = self.current_percepts['price']
        self.usage = self.current_percepts['tpnumber']
        self.age = 0
        self.usage_std = 0
        self.to_buy = 0
        self.spendings = 0
        self.price_percent = 1

    def act(self):

        tpnumber_t_1 = self.current_percepts['tpnumber']

        self.usage_std = 100
        self.price_percent = (
            self.price_average / self.current_percepts['price'])

        self.to_buy = max(self.usage_average + self.usage_std *
                          (4*self.price_percent) - self.current_percepts['tpnumber'], 0)
        self.spendings = self.to_buy * self.current_percepts['price']

        action = {'to_buy': self.to_buy}

        self.current_percepts = self.env.change_state(action)
        self.age += 1

        tpnumber_t = self.current_percepts['tpnumber']

        self.usage = tpnumber_t_1 + self.to_buy - tpnumber_t
        self.usage_average = (self.usage_average *
                              (self.age - 1) + self.usage)/self.age
        self.price_average = (self.price_average *
                              (self.age - 1) + self.price)/self.age
