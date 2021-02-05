#Angela's Version with a replit function

import random
from art import logo
from art import vs
from game_data import data

print(logo)
score = 0
continue_game = True
account_b = random.choice(data)

def format_data(account):
  """Takes the account data and returns the printable format."""
  account_name = account['name']
  account_descr = account['description']
  account_country = account['country']
  return f"{account_name}, a {account_descr} from {account_country}."
  
def check_answer(guess, a_followers, b_followers):
  """ Takes the user's guess and the followers count and returns it is correct. """
  if a_followers > b_followers:
    if guess == 'a':
      return guess == 'a'
    else:
      return guess == 'b'


#Make the game repeatable.
while continue_game:
# Generate a random account from the game data.
    account_a = account_b
    account_b = random.choice(data)
    
    if account_a == account_b:
        account_b == random.choice(data)

    print(f"COMPARE A: {format_data(account_a)}")
    print(vs)
    print(f"AGAINST B: {format_data(account_b)}")

    #ask the user for a guess of who has more followers.

    guess = input("Who has more followers? 'A' or 'B'\n").lower()

    #Check if user is correct.
    ##Check how many followers a user has.
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    #Give user feedback on their guess.
    if is_correct:
        score += 1
        print(f"You're correct! Current score: {score}.")
        
    else:
        print(f"Wrong answer. Game over. Final score: {score}.")
        continue_game = False
