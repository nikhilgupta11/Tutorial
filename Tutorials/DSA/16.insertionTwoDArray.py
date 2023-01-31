import numpy as np

arr1 = np.array([[2, 1, 2, 3], [4, 3, 2, 3], [34, 4, 4.5, -4]])

print(arr1)

# axis = 0 for Row and axis = 1 for coloumn
# we have to maintain the shape of metrix otherwise it will generate an error.
newArray = np.insert(arr1, 0, [[2, 3, 1, 4]], axis=0)

print(newArray)

newArray = np.insert(arr1, 0, [[2, 3, 1]], axis=1)

print(newArray)


# Using append method we can add a row and coloumn at the end of metrix, we can not describe the position

# for Row
newArray = np.insert(arr1, [[2, 3, 1, 4]], axis=0)

print(newArray)

# for coloumn
newArray = np.insert(arr1, [[2, 3, 1, 4]], axis=1)

print(newArray)
