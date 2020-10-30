import time, sys
from math import pi as RealPi
l = [2, 0, 67921, 0, 2919, 10, 3, 11, 3, 1000] #bigger l[4] will cause the recursion to breaak the operation, bigger l[9] will cause a very long calculation
l[1] = l[3] = int(l[9] ** (7 / 3)) #a fancy way of saying that pi1 and pi3 are also too slow
sys.setrecursionlimit(l[4] + 6)
a, b = '{}'
for i in range(0,10):exec(f'from pi{i} import pi as pi{i};t = time.time();pi = pi{i}(l[i]);print(f"pi{i}.py will calculate pi in {a}1000 * (time.time() - t){b} ms, with a mistake of {a}abs(RealPi - pi){b}")')
