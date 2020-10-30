def f(x):return x * f(x - 1) if x else 1
def pi(precision):return 640320 ** 1.5 / sum([f(6 * j) * (13591409 + 545140134 * j) / f(3 * j) / (f(j) * (-640320) ** j) ** 3 for j in range(0, precision)]) / 12
