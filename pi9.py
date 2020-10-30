def pi(precision):
    s = 0
    for i in range(0, precision):
        for j in range(0, precision):
            if (i / precision) ** 2 + (j / precision) ** 2 < 1:s += 1
    return 4 * s / precision ** 2
