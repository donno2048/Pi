def pi(precision):
  i = 2
  for j in range(1, precision + 1): i *= 4 * j ** 2 / (4 * j ** 2 - 1)
  return i
