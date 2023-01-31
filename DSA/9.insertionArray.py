from array import *

arr1 = array('i', [1, 2, 3, 44, 5, 55])
print(arr1)

# In insert function first element is index number and second is value
# arr1.insert(2, 33)
# print(arr1)


def insertion(array, index, value):
    if index <= len(array):
        array.insert(index, value)
        return array
    return "index number is wrong"


print(insertion(arr1, 6, 99))
