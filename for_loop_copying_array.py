from array import *

arr1 = array('i', [1,2,3,4,5])

arr2 = array('i', [])

for i in arr1:
    arr2.append(i)

print(arr2)