from art import logo, vs
from game_data import data
from replit import clear
import random

high_score = 0
A = None
B = None

def get_random_account():
  global A, B
  A = random.choice(data)
  B = random.choice(data)
  while A['name'] == B['name']:
    A = random.choice(data)

def higher_lower(letter):
  global high_score
  if letter.upper() == 'A':
    if A['follower_count'] > B['follower_count']:
      high_score += 1
      return True
    else:
      return False
  else:
    if B['follower_count'] > A['follower_count']:
      high_score += 1
      return True
    else:
      return False

def game():
  global high_score, A, B
  print(logo)
  gaming = True
  get_random_account()
  while gaming:
    print(
      f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(vs)
    print(
      f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")
    letter = input("Who has more followers? Type 'A' or 'B': ")
    if higher_lower(letter):
      clear()
      print(logo)
      print(f"You're right! Current score: {high_score}.")
      A = B
      B = random.choice(data)
      if A['name'] == B['name']:
        B = random.choice(data)
    else:
      clear()
      print(f"Sorry that's wrong. Final score: {high_score}")
      gaming = False


game()
