def pi(precision): return 4 * sum([4 * (-1) ** j / 5 ** (2 * j + 1) / (2 * j + 1) - (-1) ** j / 239 ** (2 * j + 1) / (2 * j + 1) for j in range(0, precision)])
