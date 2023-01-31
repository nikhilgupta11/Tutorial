list1 = [1, 2, 2, 3, 4, 5, 4, 3, 4]


def findingPairs(list, target):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] == list[j]:
                continue
            elif list[i] + list[j] == target:
                print(i, j)


findingPairs(list1, 4)
