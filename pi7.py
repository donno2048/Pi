def pi(precision):return sum([(4 / (8 * j + 1) - 2 / (8 * j + 4) - 1 / (8 * j + 5) - 1 / (8 * j + 6)) / 16 ** j for j in range(0, precision)])
