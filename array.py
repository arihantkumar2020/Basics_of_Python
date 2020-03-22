'''import array as arr

vals = arr.array()'''

from array import *
a=5

vals = array('i', [5, 9, 8, 4, 2])
#'i' for signed integer

newarr = vals
newarr2 = array(vals.typecode, (a**2 for a in vals))

vals.reverse()
print(vals)

for i in vals:
    #for i in range(len(vals)):
    print(i, end = '  ')

print("\n",newarr)

print(newarr2)

newarr2.append(int(input("Enter a number:")))
print(newarr2)

i=0
while i<len(newarr2):
    print(newarr2[i], end=' ')
    i+=1