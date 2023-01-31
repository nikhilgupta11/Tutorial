def sumOfnumbers(n):
    assert n >= 0 and int(n) == n, 'The number should be positive integer'
    if n == 0:
        return 0
    else:
        return int(n % 10) + sumOfnumbers(int(n/10))


print(sumOfnumbers(13))
