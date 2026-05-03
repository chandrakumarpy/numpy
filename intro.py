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
# my array randam and reshapr -----------------
import numpy as np
arr1 = np.random.rand(10)
print(arr1)
arr2 = np.random.randn(3,4)
print(arr2)
arr3 = np.random.randint(3,40, size= (2,3))
print(arr3)
new_arr =arr3.astype(float)
print(new_arr)
print(arr3.reshape(1,6)) # change the shape
print(arr3.ravel()) # convertoto 1 dim array
print(arr3.flatten()) # convertoto 1 dim array no connection to old
