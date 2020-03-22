#shallow copy b/w two arrays
from numpy import *

arr1 = array([2,6,8,1,3])

arr2 = arr1.view()
#memory locations of both the arrays are changed, and concept of shallow copy has been implemented

arr1[2] = 20
#change will reflect in both the arrays

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))