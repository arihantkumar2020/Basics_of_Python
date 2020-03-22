from array import *

arrlen = int(input("Enter the length of array: "))

newarr = array('i', [])

for i in range(arrlen):
    newarr.append(int(input("Enter array value: ")))

print(newarr)

c=0
for i in range(arrlen-1):
    for j in range(arrlen-i-1):
        if newarr[j] > newarr[j+1]:
            temp = newarr[j]
            newarr[j] = newarr[j+1]
            newarr[j+1] = temp

print("Sorted array : ", end='')
print(newarr)