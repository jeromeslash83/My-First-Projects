#Angela's code in the course
import random
import blackjack_art
from replit import clear

def deal_card():
  """Returns a random card from the deck of cards"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

player_card = []
dealer_card = []
for _ in range(2):
  player_card.append(deal_card())
  dealer_card.append(deal_card())


  

