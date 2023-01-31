dict1 = {'z': 1, 'd': 2}


def terverse(dictionary):
    for key in dictionary:
        print(key, dictionary(key))


terverse(dict1)
