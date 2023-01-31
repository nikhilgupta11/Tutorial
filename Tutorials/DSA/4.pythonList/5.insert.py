list1 = [3, 2, 43, 45, 5, 3, '3gf']

print(list1)

# insert:- at any given index
list1.insert(0, 44)
print(list1)


def insert(list, index, value):
    if index >= len(list):
        return "index is not valid"
    else:
        list.insert(index, value)
        return list


print(insert(list1, 3, 'hh'))

# append:- at last position
list1.append(33)
print(list1)


def append(list, value):
    list.append(value)
    return list


print(append(list1, 232))


# extend:- add another list
newlist = [3, 2, 4, 2]

list1.extend(newlist)
print(list1)


def extend(list, newlist):
    list.extend(newlist)
    return list


print(extend(list1, newlist))
