from genetic import Genetic
from pylab import *


f = lambda x, y: x**3 - 35 + x
gen = Genetic(f, minim = -15, maxim = 15)
minim = gen.run()
print('Minimum found x =', minim[0], ', f(x) =', minim[0]**3 - 35 + minim[0])