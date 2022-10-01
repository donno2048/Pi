def pi(precision): return 4 * sum((i / precision) ** 2 + (j / precision) ** 2 < 1 for j in range(0, precision) for i in range(0, precision)) / precision ** 2
