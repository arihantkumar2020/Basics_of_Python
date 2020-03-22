from array import *

arr = array('i', [])

n = int(input("Enter the length of array : "))

for i in range(n):
    arr.append(int(input("Enter element number %d : "%(i+1))))

print(arr)

arr.reverse()

newarr = array('i', [])

for i in arr:
    newarr.append(i)

print("Reversed array : ", newarr)