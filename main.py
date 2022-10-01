import time
from math import pi as RealPi
l = [2, 0, 67921, 0, 0, 10, 3, 11, 3, 1000] # bigger l[9] will cause a very long calculation
l[1] = l[3] = l[4] = int(l[9] ** 2) # a fancy way of saying that pi1, pi3 and pi4 are also too slow
for i in range(0, 10):
    t = time.perf_counter()
    pi = __import__(f'pi{i}').pi(l[i])
    print(f"pi{i}.py will calculate pi in {1000 * (time.perf_counter() - t)} ms, with a mistake of {abs(RealPi - pi)}")
