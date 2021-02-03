import random
attempts_list = []
def show_scores():
    if len(attempts_list) <= 0:
        print("There are no high scores currently in the game, you can be the one to take it!")
    else:
        print("The current high score is {} attempts".format(min(attempts_list)))
def start_game():
    random_number = int(random.randint(1, 20))
    print("Hello there gamer! Welcome to Jslash's Random Number Guessing game!")
    player = input("What is your name? ")
    want_to_play = input("Hi, {}, Do you want to play the game? (Type Yes/No) ".format(player))
    attempts = 0
    show_scores()
    while want_to_play.lower() == "yes":
        try:
            guess = input("Pick a number between 0 to 20. ")
            if int(guess) < 1 or int(guess) > 20:
                raise ValueError("Please choose a number in within the given data.") 
            if int(guess) == random_number:
                print("Congratulations! You got it!")
                attempts += 1
                attempts_list.append(attempts)
                print("It took you {} attempts to guess the correct answer".format(attempts))
                play_again = input("Would you like to play again? (Type Yes/No) ")
                attempts = 0
                show_scores()
                random_number = int(random.randint(1, 20))
                if play_again.lower() == "no":
                    print("Okay, thank you for playing", player)
                    break
            elif int(guess) > random_number:
                print("lower")
                attempts += 1
            elif int(guess) < random_number:
                print("higher")
                attempts += 1
        except ValueError as err:
            print("That's not a valid value. Try again...")
            print("({})".format(err))
    else:
        print("That's cool, have a good one!")
if __name__ == '__main__':
    start_game()
    