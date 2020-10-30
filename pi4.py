def m(l):return l[0] * m(l[1:]) if len(l) else 1
def pi(precision):return 2 * m([4 * j ** 2 / (4 * j ** 2 - 1) for j in range(1, precision + 1)])
