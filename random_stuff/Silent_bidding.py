from replit import clear
import art

bidder = True
bids ={}
while bidder == True:
  print(art.logo)
  name = input('What is your name? ')
  your_bid = int(input('What is your bid? $'))
  move_on = input("Are there any other bidder? 'yes' or 'no'\n")
  
  def new_data (person, money):
    bids[person] = money

  if move_on == 'yes':
    clear()
    new_data(person=name, money=your_bid)
  elif move_on == 'no':
    new_data(person=name, money=your_bid)
    bidder = False
    x = 0
    name = ''
    for key in bids:
      if bids[key] > x:
        x = bids[key]
        name = key
    print(f"The winner is {name} with a bid of {x}")
  else:
    print('Wrong input try again.')
      
