def pi(precision):
    a, b, t = 1, 2 ** -.5, .25
    for i in range(0, precision):
        c, d = (a + b) / 2, (a * b) ** 0.5
        t -= 2 ** i * (a - c) ** 2
        a, b = c, d
    return (a + b) ** 2 / 4 / t
