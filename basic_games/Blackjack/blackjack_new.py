import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = {'A': 1, '2': 2, '3': 3, '4': 4, 
         '5': 5, '6': 6, '7': 7, '8': 8, 
         '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

game = True

def deal_card():
    card = random.choice(list(cards.keys()))
    return card

def calculate_score(cards):
    if cards == 'A' and your_score == 10:
        return 11
    else:
        return cards

def check_winner(your_score, dealer_score):
    print(f'Your score: {your_score}')
    print(f'Dealer score: {dealer_score}')
    if your_score > 21:
        print("You lose")
    elif dealer_score > 21:
        print("You win")
    elif your_score > dealer_score:
        print("You win")
    elif your_score < dealer_score:
        print("You lose")
    else:
        print("Draw")

while game:
    start_game = None
    your_cards = []
    dealer_cards = []
    your_score = 0
    dealer_score = 0
    
    start_game = input("DO you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if start_game == 'n':
        game = False
        break
    
    print(logo)
    for i in range(2):
        your_cards.append(deal_card())
        dealer_cards.append(deal_card())
        your_score += calculate_score(cards[your_cards[i]])
        dealer_score += calculate_score(cards[dealer_cards[i]])
        
    print(f"Your cards: {your_cards}, current score: {your_score}")
    print(f"Dealer's first card: {dealer_cards[0]}")
    for i in range(5):
        hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        
        if hit == 'y':
            your_cards.append(deal_card())
            your_score += cards[your_cards[-1]]
            print(f"Your cards: {your_cards}, current score: {your_score}")
        else:
            break
        

    while dealer_score  < 17:
        dealer_cards.append(deal_card())
        dealer_score += cards[dealer_cards[-1]]
    else:
        check_winner(your_score, dealer_score)
