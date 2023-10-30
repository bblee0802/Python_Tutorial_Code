from math import *
from pylab import *

def hert(x):
    return (sqrt(cos(x)) * cos(200 * x) + sqrt(abs(x))) 

x= linspace(-1.6, 1.6, 1500)
f = lambda x: (sqrt(cos(x)) * cos(200 *x)+ sqrt(abs(x)) - 0.7) * pow((4-x*x), 0.01)
plot(x, list(map(hert,x)))    
show()