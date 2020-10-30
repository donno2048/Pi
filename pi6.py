def pi(precision):
    a = 1;b = 2 **- 0.5;t = 1 / 4
    for i in range(0, precision):c = (a + b) / 2;d = (a * b) ** 0.5;t -= 2 ** i * (a - c) ** 2;a = c;b = d
    return (a + b) ** 2 / 4 / t
