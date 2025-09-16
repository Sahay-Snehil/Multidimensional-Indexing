import numpy as np
array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])
# print(array)
# indexing array[start:end:skip]

# for  Row
print(array[0])
print(array[1])
print(array[2])
print(array[3])
print(array[0:2])
print(array[1::2])

# For Column
print(array[:,0:1])
print(array[:,1:2])
print(array[:,2:3])

# Combining Row and Column
print(array[0:2,0:2])
print(array[2:,2:])
print(array[2:,1:3])