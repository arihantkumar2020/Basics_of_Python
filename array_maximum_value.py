from array import *

arr1 = array('i', [32,1,6,4,344,32])

max = arr1[0]

for i in arr1:
    if i > max:
        max = i

print("Maximum :", max)