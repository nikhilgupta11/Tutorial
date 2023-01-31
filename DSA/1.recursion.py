# recursion -->
def powerOfTwo(n):
    if n == 0:
        return 1
    else:
        power = powerOfTwo(n-1)
        print(power)
        return 2 * power


print(powerOfTwo(5))

# iteration -->
# def powerofTwo(n):
#     i = 0
#     power = 1
#     while i < n:
#         power = power * 2
#         i = i + 1
#     return power


# print(powerofTwo(5))
