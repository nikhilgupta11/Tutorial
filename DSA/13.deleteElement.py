from array import *

arr1 = array('i', [3, 4, 3, 4, 3])

print(arr1)


def deleteElement(array, value):
    if value in array:
        array.remove(value)
        return array
    return "value is not available"


print(deleteElement(arr1, 4))
