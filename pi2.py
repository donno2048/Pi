def pi(precision): return 3 + sum([(-1) ** j / (2 * j ** 2 - 3 * j + 1) / j for j in range(2, precision + 2)])
