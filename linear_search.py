from array import *

arr = array('i', [])

n = int(input("Enter the length of array: "))

for i in range(n):
    x = int(input("Enter the array value %d : "%(i+1)))
    arr.append(x)

print(arr)

val = int(input("Enter the value for search: "))

k=0
for i in arr:
    if i==val :
        print(k)
        break
    k+=1
else:
    print("element not found")

#print(arr.index(val)) but it will show error if element not found