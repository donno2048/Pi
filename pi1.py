def pi(precision):return 4 * sum([(1 - 2 * (j % 2)) / (2 * j + 1) for j in range(0, precision)])
