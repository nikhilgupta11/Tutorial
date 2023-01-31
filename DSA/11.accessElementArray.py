from array import *

arr1 = array('d', [1.2, 4, 3, 45, 4, 3])

print(arr1)


def accessElement(array, index):
    if index >= len(array):
        print("There is no element at this location")
    else:
        print(array[index])


accessElement(arr1, 5)
accessElement(arr1, 6)

# here length of array is 6 so if we defien the index 6 then it willl generate an exception
# to spolve this problem we have to use equal to sign
