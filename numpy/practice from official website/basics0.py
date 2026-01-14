import numpy as np
import pandas as pd
from numpy import pi
from numpy import random as rg
#numpy array are called ndarray

"""numpy np.array can handle multidimentional array but the array.array can only handle 
one dimentional array 
"""
print("-"*70)

data = np.array([[1,2,3],
                [4,5,6]]) # 2 axix and 6 elements and lenght of 2

# 3d space means direction in python where:
# x  = left,right
# y = forward, backward
# z = up,down

print("data type:", type(data))
print("size: ",np.size(data))
print("shape: ",np.shape(data))
print("lenght: ",len(data))
print("actual data: ",data)

print("-"*70)
value = np.array([[0,0,0],
                  [0,0,0]], dtype=np.int16)

print(value)
print("-"*70)


print(np.zeros(3, int))
print("-"*70)

# print(np.zero((3,4, int)))
print(np.ones(3,int))
print("-"*70)


x = np.linspace(0,2*pi,100)
f = np.sin(x)
print(x)
print(f)

print("-"*70)


a = np.arange(8).reshape(2,2,2)  #3d reshape()
b = np.arange(8).reshape(4,2)
c = np.arange(8).reshape(1,8) #1d reshape(row,column) 
"""or:
c = np.arange(8) == c = np.arange(8).reshape(1,8) """

print("3d: ",a)
print("2d: ", b)
print("1d: ", c)
print("-"*70)

print("sum: ", a.sum())
print("min: ",a.min())
print("max: ",a.max())
print("-"*70)

"""in reshape(row,column), arange() -> creates list inclusing numerical value starting from 0 to n"""

d = rg.random((2,3))

print("random value: ",d)

print("-"*70)
