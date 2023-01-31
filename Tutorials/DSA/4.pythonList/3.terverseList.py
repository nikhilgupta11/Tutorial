list1 = [1, 2, 3, 2, 3, 4]

print(list1)


def terverseList(list):
    for i in list:
        print(i)
        # return i
        # return only reurn a single element from operation, whereas the print statment print all the given values. thats why we always use print statement during terverse operations.


terverseList(list1)
# print(terverseList(list1))

# For perform any mathematical operations on values we cannot use simple loop on list.


def terverseList(list):
    for i in range(len(list)):
        print(str(list[i])+"+")


terverseList(list1)
