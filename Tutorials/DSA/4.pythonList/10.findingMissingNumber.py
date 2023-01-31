
list1 = [1, 2, 3, 4, 5, 6, 7, 9, 10]


def missingNumber(list1, n):
    sum1 = n*(n+1)/2
    sum2 = sum(list1)
    print(sum1-sum2)


missingNumber(list1, 10)
