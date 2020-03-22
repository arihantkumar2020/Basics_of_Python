from numpy import *

n = int(input("Enter the total number of elements in each array : "))

print("Enter elements of array 1: -")

arr1 = []

for i in range(n):
  arr1.append(int(input("Enter array element %d : "%(i+1))))

arr1 = array(arr1)

print("Enter elements of array 2: -")

arr2 = []

for i in range(n):
  arr2.append(int(input("Enter array element %d : "%(i+1))))

arr2 = array(arr2)

arr3 = []

for i in range(n):
  arr3.append(0)

arr3 = array(arr3)

arr1 = arr1.reshape(3,3)
arr2 = arr2.reshape(3,3)
arr3 = arr3.reshape(3,3)

for i in range(3):
  for j in range(3):
    for k in range(3):
      arr3[i][j] = arr3[i][j] + arr1[i][k] * arr2[k][j]

for i in range(3):
  for j in range(3):
    print(arr3[i][j], end = ' ')
  print()