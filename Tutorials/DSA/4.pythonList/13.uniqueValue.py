

list1 = [2, 1, 32, 4, 2, 4, 2, 3, 3]
list2 = [1, 2, 3, 4]


def uniqueValue(list):
    a = []
    for i in list:
        if i in a:
            print(i)
        else:
            a.append(i)
    print(a)


uniqueValue(list2)
