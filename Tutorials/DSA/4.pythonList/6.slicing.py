

list1 = [2, 2, 2, 3, [32, 2], 2]

print(list1)

# will print complete list
print(list1[:])

# print element wit index 0 and 1
print(list1[0:2])

# exclude the last element and print the rest
print(list1[:-1])

# updation of multiple element using slicing,
list1[0:2] = ['r', 'r']
print(list1)

# if we have more value then required, then it will automatically add the rest of vlaues after the sliced value
list1[0:2] = ['r', 'r', 'r']
print(list1)


def slicing(list, value):
    return list[(value)]


print(slicing(list1, ':'))
