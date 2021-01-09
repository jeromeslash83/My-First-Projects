print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
price = 0
while True:
  if size == 'S':
    price = 15
    if add_pepperoni == 'Y':
      price += 2
    elif add_pepperoni == 'N':
      price += 0
    else :
      print('You have typed a wrong input.')
  elif size == 'M':
    price = 20
    if add_pepperoni == 'Y':
      price += 3
    elif add_pepperoni == 'N':
      price += 0
    else :
      print('You have typed a wrong input.')
  elif size == 'L':
    price = 25
    if add_pepperoni == 'Y':
      price += 3
    elif add_pepperoni == 'N':
      price += 0
    else :
      print('You have typed a wrong input.')
  else :
    print('You have typed a wrong input.')

  if extra_cheese == 'Y':
    price += 1
  elif extra_cheese == 'N':
    price += 0
  else :
    print('You have typed a wrong input.')

  print(f'Your final bill is: ${price}.')
