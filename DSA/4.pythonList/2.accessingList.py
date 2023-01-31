list1 = [2, 3, 4, 3, 2, 3, 'fgf']

print(list1)


def accessList(list, index):
    if index >= len(list):
        return "item is not available"
    else:
        return list[index]


print(accessList(list1, 7))

# In operator:- using this operator we can check that the element is available or not in data, if available it will return true otherwise false.

print(4 in list1)


def inOperator(list, element):
    for i in list:
        if i == element:
            return "true"
    return "item not available"


print(inOperator(list1, 4))


# Back slicing
print(list1[1])

# making suslist from a list
print(list1[:1])
# this will print the first element as a list
