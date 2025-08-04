#testing numpy

import numpy as np   #importing numpy library

A = np.array(5)  # scaler array
np.ndim(A)  #dimension method (it tells the dimension of the array
print(np.ndim(A))
print(A)

one = np.array([1,2,2,3,4])
print(np.ndim(one))
print(one)

two = np.array([[1,2,3,4],[2,3,45,9]])
print(np.ndim(two))
print(two)
three = np.array([[[1,2,34],[2,24,423],[2,43,56]]])
print(np.ndim(three))
print(three)

arr = np.array([1,2,3,'Anupam'])  #automatic type conversion
print(arr)
print(type(arr))

#reshapping of arrays
ay = np.array([1,2,3,4,5,6,7,8,9,0,11,21])
print(ay)
newarr = ay.reshape(2,3,2)
print(newarr)

# print(newarr[2,0])