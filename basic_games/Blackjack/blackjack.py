import random
import blackjack_art
cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K","A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
def addition(card_1, card_2):
    return card_1 + card_2
def blackjack():
    total = 0
    dealer_total = 0
    player = []
    dealer = []
    extra_dealern = 0
    print('Welcome to J Casino Blackjack')
    playing = True
    while playing:
        start = input('Would you like to play a game?\n"y" or "n": ')
        if start == "y":
            print(blackjack_art.logo)
            your_card = random.sample(cards, 2)
            player.append(your_card[0])
            player.append(your_card[1])
            print(f'Your cards are: {player}.')
            for num in range(0,2):
                your_card[num]
                if your_card[num] == 'J' or your_card[num] == 'Q' or your_card[num] == 'K':
                    your_card[num] = 10
                elif your_card[num] == 'A':
                    your_card[num] = 11
                else:
                    your_card[num] = your_card[num]
            total = addition(your_card[0], your_card[1])
            if total == 22:
                total -= 10
            print(f"Your total is {total}")

            dealer_card1 = random.choice(cards)
            dealer.append(dealer_card1)
            if dealer_card1 == 'J' or dealer_card1 == 'Q' or dealer_card1 == 'K':
                dealer_card1n = 10
            elif dealer_card1 == 'A':
                dealer_card1n = 11
            else:
                dealer_card1n = dealer_card1
            dealer_total = dealer_card1n
            print(f"The dealer's card is {dealer}.")
            print(f"Dealer's total score is {dealer_total}.")

            another_card = input("Would you like to draw another card?\n'y' or 'n': ")
            if another_card == 'y':
                bonus_card = random.choice(cards)
                player.append(bonus_card)
                if bonus_card == 'J' or bonus_card == 'Q' or bonus_card == 'K':
                    bonus_cardn = 10
                elif bonus_card == 'A':
                    bonus_cardn = 1
                else:
                    bonus_cardn = bonus_card
                total = addition(total, bonus_cardn)
                dealer_card2 = random.choice(cards)
                dealer.append(dealer_card2)
                if dealer_card2 == 'J' or dealer_card2 == 'Q' or dealer_card2 == 'K':
                    dealer_card2n = 10
                elif dealer_card2 == 'A':
                    if dealer_total == 11:
                        dealer_card2n = 1
                    else:
                        dealer_card2n = 11
                else:
                    dealer_card2n = dealer_card2
            elif another_card == 'n':
                dealer_card2 = random.choice(cards)
                dealer.append(dealer_card2)
                if dealer_card2 == 'J' or dealer_card2 == 'Q' or dealer_card2 == 'K':
                    dealer_card2n = 10
                elif dealer_card2 == 'A':
                    dealer_card2n = 11
                else:
                    dealer_card2n = dealer_card2
            else:
                print("Wrong input. Try again.")
                another_card = input("Would you like to draw another card?\n'y' or 'n': ")
            dealer_total = addition(dealer_card1n, dealer_card2n)
            if dealer_total < 17:
                extra_dealer = random.choice(cards)
                dealer.append(extra_dealer)
                if extra_dealer == 'J' or extra_dealer == 'Q' or extra_dealer == 'K':
                    extra_dealern = 10
                elif extra_dealer == 'A':
                    extra_dealern = 1
                else:
                    extra_dealern = extra_dealer
            dealer_total = addition(dealer_total, extra_dealern)
            print(f"Your cards: {player}")
            print(f"Dealer's cards: {dealer}")
            print(f"Your total: {total}")
            print(f"Dealer's total: {dealer_total}")
            if total > dealer_total:
                if total > 21 and dealer_total > 21:
                    print("Tie.")
                elif total > 21:
                    print("You lose.")
                else:
                    print("You win.")
            elif total < dealer_total:
                if total > 21 and dealer_total > 21:
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
            playing = False

blackjack()
