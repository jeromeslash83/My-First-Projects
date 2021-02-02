#Angela's code in the course
import random
import blackjack_art
from replit import clear

def deal_card():
  """Returns a random card from the deck of cards"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Takes a list of cards as an input and calculates their score"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  
  if 11 in cards and sum(cards) > 21:
    cards.remove 11
    cards.append 1
  return sum(cards)

def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"


  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"
    

def blackjack():
  print(logo)
  player_card = []
  dealer_card = []
  is_game_over = False
  for _ in range(2):
    player_card.append(deal_card())
    dealer_card.append(deal_card())

  while not is_game_over:
    player_total = calculate_score(player_card)
    dealer_total = calculate_score(dealer_card)

    print(f" Your cards: {player_card}  Your current score: {player_total}")
    print(f" Dealer's cards: {dealer_card[0]} , _ ")


    if player_total == 0 or dealer_total == 0 or player_total > 21:
      is_game_over = True
    else:
      hit_me = input("Do you want another card?\n'y' or 'n': ")
      if hit_me == 'y':
        player_card.append(deal_card())
      elif hit_me == 'n':
        is_game_over = True
      else:
        print("Wrong input. Try again.)
        hit_me = input("Do you want another card?\n'y' or 'n': ")

  if dealer_total != 0 and dealer_total < 17:
    dealer_card.append(deal_card())
    dealer_total = calculate_score(dealer_card)
  
  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score)
              
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
            
  
            
            
    
    

  

