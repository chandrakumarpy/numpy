import numpy as np
data = [1,3,-1,3,-5,7]
d1 = np.array(data)
print(d1.dtype)
d1[d1<0] =0
d1[1] = 10
print(d1.ndim)
d1 = np.array(data, dtype = complex)
print(d1)
d2 = np.arange(0,100, 4)
print(d2)
d3 = np.linspace(0,1,10)
print(d3)
d4 = np.logspace(0,10, 3)
print(d4)
d5 = np.zeros([3,4])
print(d5)
d6 = np.ones([3,4])
print(d6)
print(d5+d6)
d7 = np.full([2,3], 8)
print(d7)
