from numpy import *

arr1 = array([
  [1,2,3,6,2,9],
  [4,5,6,7,5,3]
])

print(arr1)

print(arr1.dtype)
#dtype gives the data type of the elements stored in the array

print(arr1.ndim)
#ndim gives the number of dimensions in the array

print(arr1.shape)
#shape returns a tuple with number of rows and number of columns

print(arr1.size)
#returns the entire size of the array

arr2 = arr1.flatten()
#flatten() converts multidimensional array into single dimensional

print(arr2)

arr3 = arr1.reshape(3,4)
#reshape converts single dimensional array into multidimensional array

print(arr3)

arr4 = arr2.reshape(2,2,3)
#now a 3d array contains two 2d arrays

print(arr4)