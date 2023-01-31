def factorial(n):
    assert n >= 0 and int(n) == n, 'the numbermust be positive only'
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(10))

# these both will generate an error
# print(factorial(-3))
# print(factorial(3.4))
