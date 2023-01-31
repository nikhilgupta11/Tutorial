list1 = [3, 2, 4, 2, 4, 3]

print(list1)

# it will pop the last item from list
list1.pop()
print(list1)

# it will pop the given index number item
list1.pop(2)
print(list1)

# we can also print the popped item
print(list1.pop())

list2 = [3, 2, 4, 24, 3, 4, 3]
# will delete only one item
del list2[1]
print(list2)

# deletion using slicing
del list2[0:2]
print(list2)

# remove method work on value, it will delete the first value it find
list2.remove(3)
print(list2)


def remove(list, value):
    for i in list:
        if i == value:
            list.remove(3)
            return list
    return "value not found"


print(remove(list2, 3))
print(remove(list2, 33))
