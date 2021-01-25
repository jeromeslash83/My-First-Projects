#CALCULATOR APP
def add(n1, n2):
  return n1 + n2

def subtract(n1,n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2


loop = True
n1 = int(input("What's the first number? "))

while loop:

  operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
  }
  
  for symbol in operations:
    print(symbol)

  to_do = input("What operation are we gonna do? ")
  if to_do in operations:
    operational = True
  else:
    print('Wrong input try again.')
    to_do = input("What operation are we gonna do? ")
    
  n2 = int(input("What's the next number? "))

  answer = operations[to_do](n1, n2)

  print(f"{n1} {to_do} {n2} = {answer}")

  cont = input(f"Do you want to continue with calculations with {answer}?\n'y' or 'n': ")
  if cont.lower() == 'y':
    n1 = answer
  elif cont.lower() == 'n':
    calc = input("Do you want to start a new calculation? 'y' or 'n':\n")
    if calc.lower() == 'n':
      loop = False
    elif calc.lower() == 'y':
      n1 = int(input("What's the first number? "))
    else:
      print('Wrong input. Try again')
      calc = input("Do you want to start a new calculation? 'y' or 'n':\n")
  else:
    print("Wrong input try again.")
    cont = input(f"Do you want to continue with calculations with {answer}?\n'y' or 'n': y")
