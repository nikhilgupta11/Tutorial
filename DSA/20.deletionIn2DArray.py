import numpy as np

arr1 = np.array([[5, 4, 5, 3], [4, 3, 4, 3], [4, 3, 4, 3], [7, 6, 8, 6]])

print(arr1)

# Row deletion
deletedArray = np.delete(arr1, 0, axis=0)

print(deletedArray)

# Coloumn deletion
deletedArray = np.delete(arr1, 0, axis=1)

print(deletedArray)
