from numpy import *

arr1 = array([
  [1,2,3,6],
  [4,5,6,7]
])

m = matrix(arr1)
#conversion of 2d array into matrix offers more functionality

print(m)

m2 = matrix(['1 2 3 6; 4 5 6 7'])
#in case we do not have a multidimensional array, or we are taking values from user

print(m2)

m3 = matrix(['1 2 3 ; 6 4 5 ; 1 6 7'])

print(m3)

print(diagonal(m3))
#prints diagonal elements of the matrix

print(min(m3))
#prints minimum

print(max(m3))
#prints maximum