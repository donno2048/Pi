def f(x):return x * f(x - 1) if x else 1
def pi(precision):return 9801 / sum([f(4 * j) * (1103 + 26390 * j) / (f(j) * 396 ** j) ** 4 for j in range(0, precision)]) / 2 ** 1.5
