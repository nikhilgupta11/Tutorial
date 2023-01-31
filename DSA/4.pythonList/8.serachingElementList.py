list1 = [3, 2, 432, 3, 2, 32, [3, 3, 2]]


# in operator only search for the first value
# return true and false
print(20 in list1)

if 3 in list1:
    print("available and index is " + str(list1.index(3)))
else:
    print("not available")


# linear serch
def serching(list, value):
    for i in list:
        if i == value:
            return list.index(value)
    return "value not availbale"


print(serching(list1, 3))
