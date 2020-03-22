from numpy import *

arr1 = array([2,6,8,1,3])

arr2 = arr1
#both the arrays have same memory locations, concept called aliasing

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))

