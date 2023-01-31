# exm:- liar permutation of airl

list1 = [2, 1, 2]
list2 = [2, 2, 1]


def premutation(list1, list2):
    if len(list1) == len(list2):
        list1.sort()
        list2.sort()
        if list1 == list2:
            print("premutation true")
            return True
    else:
        print("not permuted")
        return False


print(premutation(list1, list2))
