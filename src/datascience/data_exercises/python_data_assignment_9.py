# Graphical Representation of numpy.linspace() using matplotlib module – pylab
# Graphical Represenation of numpy.linspace()
import numpy as geek
import pylab as p

# Start = 0
# End = 2
# Samples to generate = 10
x1 = geek.linspace(0, 2, 10, endpoint=False)
y1 = geek.ones(10)

p.plot(x1, y1, '*')
p.xlim(-0.2, 1.8)
