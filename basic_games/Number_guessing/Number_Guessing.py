import random
game_ongoing = True
def guessing_game():
    def repeat():
        loop = True
        while loop:
            new_game = input("Do you want to play another game?\n'y' or 'n': ")
            if new_game == 'y':
                guessing_game()
            elif new_game == 'n':
                print("Okay. Have a nice day!")
                global game_ongoing
                game_ongoing = False
                loop = False
            else:
                print('Wrong input. Try again.')
    print("Welcome to the Number Guessing Game.")
    print("I'm thinking of a number between 1 to 100.")
    while game_ongoing:
        difficulty = input("Choose a difficulty between 'easy' and 'hard':\n")
        easy = 10
        hard = 5
        random_number = random.randint(1,101)
        if difficulty == 'easy':
            while easy != 0:
                guess = int(input("Guess the number:"))
                if guess > random_number:
                    print('Lower.')
                    easy -= 1
                elif guess < random_number:
                    print('Higher.')
                    easy -= 1
                elif guess == random_number:
                    print("You've guessed it correctly, you win!")
                    repeat()
                    easy = 0
                else:
                    print('Wrong input. Try again.')
                print(f"You have {easy} chances left.")
            print("You lost chances. Game over.")
            repeat()
        elif difficulty == 'hard':
            while hard != 0:
                guess = int(input("Guess the number:"))
                if guess > random_number:
                    print('Lower.')
                    hard -= 1
                elif guess < random_number:
                    print('Higher.')
                    hard -= 1
                elif guess == random_number:
                    print("You've guessed it correctly, you win!")
                    repeat()
                    hard = 0
                else:
                    print('Wrong input. Try again.')
                print(f"You have {hard} chances left.")
            print("You lost chances. Game over.")
            repeat()
        else:
            print('Wrong input. Try again.')
guessing_game()
