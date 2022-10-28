#create your own ufunc
import numpy as np
def myadd(x, y):
    return x+y
myadd= np.frompyfunc(myadd, 2, 1)
print(myadd([1, 2, 3, 4],[5, 6, 7, 8]))

#simple arthematic
import numpy as np
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.add(arr1, arr2)# apply to sub,multiply,mod,div
print(newarr)

#rounding decimals
import numpy as np
arr= np.floor([-3.1666, 3.6667])
print(arr)#reduce the value to lower digits.

import numpy as np
arr= np.ceil([-3.1666, 3.6667])
print(arr)#raise value into upper digits

#numpy Logs
import numpy as np
arr = np.arange(1, 10)
print(np.log(arr))

#SUMMATIONS Numpy
import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([1, 2, 3, 5])
newarr = np.sum([arr1, arr2])
print(newarr)
#cummulative sum
import numpy as np
arr = np.array([1, 2, 3])
newarr = np.cumsum([1, 2, 3])
print(newarr)

#Finding L.C.M
import numpy as np
num1 = 4
num2 = 6
x = np.lcm(num1,num2)
print(x)
#finding lcm in arrays
import numpy as np
arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr)
print(x)

#finding GCD
import numpy as np
num1 = 6
num2 = 9
x = np.gcd(num1, num2)
print(x)
#finding the GCD in arrays
import numpy as np
arr = np.array([20, 8, 32, 36, 16])
x = np.gcd.reduce(arr)
print(x)

#Trigonometric functions
import numpy as np
x = np.sin(np.pi/2)
print(x)
#find sine values for all oof the values
import numpy as np
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sin(arr)
print(x)
#finding angles
import numpy as np
x = np.arcsin(1.0)
print(x)
#angles of each array
import numpy as np
arr = np.array([1, -1, 0.1])
x = np.arcsin(arr)
print(x)

#Numpy Set Operations
import numpy as np
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)
print(x)
#finding intersection
import numpy as np
arr1 = np.array([1,2,3,4])
arr2 = np.array([3,4,5,6])
newarr = np.intersect1d(arr1, arr2,assume_unique=True)
print(newarr) 
#finding Difference
import numpy as np
set1 = np.array([1,2,3,4])
set2 = np.array([3,4,5,6])
newarr = np.setdiff1d(set1,set2,assume_unique=True)
print(newarr)