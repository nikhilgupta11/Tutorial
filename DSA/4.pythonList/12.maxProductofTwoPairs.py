import numpy as np

array1 = np.array([2, 1, 3, 2, 43, 2, 3, 2])


def maxProductOfTwoPairs(array):
    maxProd = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] * array[j] > maxProd:
                maxProd = array[i] * array[j]
                pairs = str(array[i]) + "," + str(array[j])
    print(pairs)
    print(maxProd)


maxProductOfTwoPairs(array1)
