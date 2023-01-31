import numpy as np

arr1 = np.array([[32, 3, 3, 2], [3, 3, 2, 4], [5, 54, 33, 4], [5, 4, 3, 3]])

print(arr1)

# here we will take only one argument in function beacuse terversal is going through all the metrix, so no need to specify the rowIndex and colIndex


def terversal(array):
    for i in range(len(array)):
        # \n for gapping between the rows
        print("\n")
        for j in range(len(array[0])):
            print(array[i][j])


terversal(arr1)
