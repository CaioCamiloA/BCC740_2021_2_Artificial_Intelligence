from environments import ToilletPaperEnv
from agents import ToilletPaperAg
import numpy as np
import matplotlib.pyplot as plt

env1 = ToilletPaperEnv(10, 1000, 1000)

agent = ToilletPaperAg(env1)

prices = []
tpnumber = []
spendings = []
price_percent = []

for i in range(1000):
    prices.append(env1.price)
    tpnumber.append(env1.TPNumber)
    spendings.append(agent.spendings)
    price_percent.append(agent.price_percent)
    agent.act()

plt.plot(prices)
plt.show()
plt.plot(price_percent)
plt.show()
plt.plot(tpnumber)
plt.show()
plt.plot(spendings)
plt.show()

cumspe = np.cumsum(spendings)
plt.plot(cumspe)
plt.show()
