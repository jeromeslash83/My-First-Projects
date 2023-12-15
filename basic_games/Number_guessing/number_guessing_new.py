import random

lives = 10
number = random.randint(1, 100)

def difficulty(answer):
    if answer == "easy":
        return 10
    elif answer == "hard":
        return 5
    else:
        return "Invalid difficulty"
    
def guess_number(guess):
    global number, lives
    if guess == number:
        print(f'You got it!, the number was {number}')
        lives = 0
    elif guess > number:
        print("Too high\nGuess again")
        lives -= 1
    else:
        print("Too low\nGuess again")
        lives -= 1

  
def game(): 
    global lives, number  
    print("Welcome to the Guessing Game!\nI'm Thinking of a number betwen 1 and 100")
    
    lives = difficulty(input("Choose a difficulty. Type 'easy' or 'hard': "))

    while lives != 0:
        print(f'Your have {lives} attempts remaining to guess the number')
        guess = int(input("Make a guess: "))
        guess_number(guess)
        if lives == 0 and guess != number:
            print("You've run out of guesses, you lose.")
    
game()
