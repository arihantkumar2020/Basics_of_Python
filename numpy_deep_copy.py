#deep copy b/w two arrays
from numpy import *

arr1 = array([2,6,8,1,3])

arr2 = arr1.copy()
#memory locations of both the arrays are changed, and concept of deep copy has been implemented

arr1[2] = 20
#change will reflect only in arr1

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))