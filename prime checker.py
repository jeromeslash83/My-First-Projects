import math
def prime_checker(number):
  if n<2:
    return False
  elif n == 2:
    return True
  else:
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
      if n % i == 0:
        return False

    return True
