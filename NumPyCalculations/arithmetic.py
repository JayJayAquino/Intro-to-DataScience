import numpy as np
from numpy.random import randn

np.set_printoptions(precision=2)

a = np.array([1,2,3,4,5,6])
print(a)
b = np.array([[10,20,30], [40,50,60]])
print(b)

np.random.seed(25)
c = 36*np.random.randn(6)
print(c)

d = np.arange(1,35)
print(d)
