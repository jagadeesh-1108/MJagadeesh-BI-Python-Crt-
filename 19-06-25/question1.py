# write a python programme to create 1 dimensional array with 15 elements and reshape into 2 dimensional array with 3 rows and 5 col
#5 rows and 3 col and print the dimension of it reshape the same array into 3 dimensional array with 5 rows and 3 col with 1 element in each colounm
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(arr)
print(arr.ndim)
newarr = arr.reshape(3,5)
print(newarr)
newarr2=arr.reshape(5,3)
print(newarr2.ndim)
newarr3=arr.reshape(5,3,1)
print(newarr3)
print(newarr3.ndim)