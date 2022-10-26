import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr)
print(type(arr))

#checking numpy version
import numpy as np
print(np.__version__)

#2-D Arrays
import numpy as np
arr = np.array([[1, 2, 3,],[4, 5, 6]])
print(arr)

#check number of dimensions
import numpy as np
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#Array Indexing
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[1])

#Acess the element of the first row,second column
import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1])

#Python slicing.
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

#checking the data type of an array
import numpy as np
arr = np.array([7, 8 , 9, 10, 11])
print(arr.dtype)

#numpy array copy vs view
#COPY
import numpy as np
arr = np.array([5, 6, 7, 8, 9])
x = arr.copy()
arr[0]= 42
arr[3]= 89
print(arr)
print(x)

#VIEW
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
x = arr.view()
arr[2] = 67
print(arr)
print(x)

#Check if Array Owns its Data
import numpy as np
arr = np.array([3, 4, 5, 6,7])
x = arr.copy()
y = arr.view()
print(x.base)
print(y.base)

#get the shape of an Array
import numpy as np
arr = np.array([[1, 2, 3, 4,],[5, 6, 7, 8]])
print(arr.shape)

#Numpy Array  Reshaping
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(2, 6)# rows and columns
print(newarr)

#Numpy Array Iterating..means going through an array one by one
import numpy as np
arr = np.array([1, 2, 3])
for x in arr:
  print(x)

#Numpy joining Arrays
  import numpy as np
  arr1 = np.array([1,2,3])
  arr2 = np.array([4,5,6])
  arr = np.concatenate((arr1,arr2))
  print(arr)

  #Python splitting Arrays
  import numpy as np
  arr = np.array([1,2,3,4,5,6])
  newarr = np.array_split(arr,3)
  print(newarr)

  #Numpy searching Arrays
  import numpy as np
  arr = np.array([1,2,3,4,5,4,4])
  x = np.where(arr ==4)
  print(x)# print index which 4 is present

  #Numpy Sorted Arrays
  import numpy as np
  arr = np.array([[3,1,6],[4,0,2]])
  print(np.sort(arr))

  #Numpy Filter Array
  import numpy as np
  arr = np.array([41, 42, 43, 44])
  x = [True,False,True,False]
  newarr = arr[x]
  print(newarr)

  #Creating the Filter ARRAY
import numpy as np
arr = np.array([41, 42, 43, 44])
filter_arr = []# Create an empty list
for element in arr:# go through each element in arr
  if element > 42:# if the element is higher than 42, set the value to True, otherwise False:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

#Getting Randoms number in Numpy
from numpy import random

x = random.randint(100)

print(x)
