
import numpy as np

arr1 = np.array([[1, 2, 4, 4], [4, 5, 3, 5], [
                65, 76, 56, 78], [65, 44, 33, 4]])
print(arr1)


def accessElement(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        print("you have entered the wrong input")
    else:
        print(array[rowIndex][colIndex])


accessElement(arr1, 3, 3)

# this will print if statement in result
accessElement(arr1, 4, 4)
