list1 = [3, 2, 4, 3, 4, 3]

list1[3] = 'gfg'

print(list1)


def updateElement(list, index, value):
    if index >= len(list):
        return "value of index is not right"
    else:
        list[index] = value
        return list1


print(updateElement(list1, 3, 'tt'))
