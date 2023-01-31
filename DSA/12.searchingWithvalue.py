from array import *

arr1 = array('f', [3, 2, 4, 3.4, 5, 3, 4])

print(arr1)


def elementsearch(array, value):
    for i in array:
        if i == value:
            # return array[int(i)]  it will give the value at 4th index
            return array.index(i)
    return "Value is not available"


print(elementsearch(arr1, 4))
