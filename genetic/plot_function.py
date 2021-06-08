import matplotlib.pyplot as plt
from pylab import *

x = linspace(-15, 15, 100)
y = x**3 - 35 + x

plot(x, y)

show()