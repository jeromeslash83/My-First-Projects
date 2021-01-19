divis = [2, 3, 5, 7]
def prime_checker(number):
  if n % n == 0:
    if n in divis:
      print("It's a prime number.")
    elif n not in divis:
      if n % 2 == 0:
        print("It's not a prime number.")
      elif n % 3 == 0:
        print("It's not a prime number.")
      elif n % 5 == 0:
        print("It's not a prime number.")
      elif n % 7 == 0:
        print("It's not a prime number.")
      else:
        print("It's a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)
