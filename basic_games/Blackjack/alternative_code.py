#BLACKJACK GAME ALTERNATIVE CODE
import random
def blackjack():
    cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K","A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    def deal():
        card = random.choice(cards)
        return card

    def addition(card1, card2):
        if card1 >= 11 and card2 == 11:
            card2 = 1
        total = card1 + card2
        return total

    def convert_player_card():
        for card in player_card:
            if card == "J" or card == "Q" or card == "K":
                card = 10
            elif card == "A":
                card = 11
            else: 
                card = card
            player_number_equivalent.append(card)

    def convert_dealer_card():
        for card in dealer_card:
            if card == "J" or card == "Q" or card == "K":
                card = 10
            elif card == "A":
                card = 11
            else: 
                card = card
            dealer_number_equivalent.append(card)
    player_card = []
    player_number_equivalent = []
    dealer_number_equivalent = []
    dealer_card = []
    loop = True
    while loop:
        print('Welcome to J Casino Blackjack')
        start = input('Would you like to play a game?\n"y" or "n": ')

        if start == 'y':
            player_card.append(deal())
            player_card.append(deal())
            dealer_card.append(deal())
            print(f"Your cards: {player_card}")
            print(f"Dealer's card:{dealer_card}")
            more_card = input("Do you want another card?\n'y' or 'n' ")
            if more_card == 'y':
                player_card.append(deal())
                dealer_card.append(deal())
                print(f"Your cards: {player_card}")
                print(f"Dealer's cards:{dealer_card}")
                convert_player_card()
                convert_dealer_card()
                total = addition(player_number_equivalent[0], player_number_equivalent[1])
                player_total = addition(total, player_number_equivalent[2])
                print(f'Your total: {player_total}')
                dealer_total = addition(dealer_number_equivalent[0], dealer_number_equivalent[1])
                if dealer_total <= 17:
                    dealer_card.append(deal())
                    print(f"Dealer's cards:{dealer_card}")
                    convert_dealer_card()
                    dealer_total = addition(dealer_total, dealer_number_equivalent[2])
                print(f"Dealer's total: {dealer_total}")
            elif more_card == 'n':
                dealer_card.append(deal())
                print(f"Your cards: {player_card}")
                print(f"Dealer's cards:{dealer_card}")
                convert_player_card()
                convert_dealer_card()
                player_total = addition(player_number_equivalent[0], player_number_equivalent[1])
                print(f'Your total: {player_total}')
                dealer_total = addition(dealer_number_equivalent[0], dealer_number_equivalent[1])
                if dealer_total <= 17:
                    dealer_card.append(deal())
                    print(f"Dealer's cards:{dealer_card}")
                    convert_dealer_card()
                    dealer_total = addition(dealer_total, dealer_number_equivalent[2])
                print(f"Dealer's total: {dealer_total}")
            else:
                print('Wrong input')
                more_card = input("Do you want another card?\n'y' or 'n'")

            if player_total > dealer_total:
                if player_total > 21 and dealer_total > 21:
                    print("Tie.")
                elif player_total > 21:
                    print("You lose.")
                else:
                    print("You win.")
            elif player_total < dealer_total:
                if player_total > 21 and dealer_total > 21:
                    print("Tie")
                elif dealer_total > 21:
                    print("You win.")
                else:
                    print("You lose.")
            else:
                print("Tie.")
            repeat = input("Do you want to play again?\n'y' or 'n': ")
            if repeat == 'y':
                blackjack()
            else:
                break
        else:
            loop = False
blackjack()
