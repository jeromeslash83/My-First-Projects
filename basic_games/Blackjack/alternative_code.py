#BLACKJACK GAME ALTERNATIVE CODE
import random
cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
print("Welcome to BlackJack!")

def deal():
    card = random.choice(cards)
    return card

def addition(card1, card2):
    total = card1 + card2
    return total
