import numpy as np

arr1 = np.array([[2, 3, 2, 4], [6, 7, 5, 6], [6, 5, 4, 6], [56, 6, 5, 4]])

print(arr1)


def searchingElement(array, element):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == element:
                return "the element has found at" + str(i) + " " + str(j)
    return "element doesnot exist"


print(searchingElement(arr1, 6))

# if we will not use the range function here the it will show an error thar int obejet is not iterable. beacuse len(array) is a fixed value so we can not iterate from it.
