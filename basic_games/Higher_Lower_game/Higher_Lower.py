#HIGHER LOWER GAME

#Import the files needed in the program.
import random
from game_data import data
import art

#Set the first two choices of A and B and the current score which is 0.
high_score = 0
game = True
A = random.choice(data)
B = random.choice(data)
def choices(a,b):
    print(f"Compare A: {a['name']}, a {a['description']} from {a['country']}.")
    print(art.vs)
    print(f"Against B: {b['name']}, a {b['description']} from {b['country']}.")
# Loop the game
while game:
    choices(A,B)
    guess = input("Who has more followers? 'A' or 'B'\n")
    
    #create a function which compares the followers of A from B.
    def compare_followers(a,b):
        if a['follower_count'] > b['follower_count']:
            return 'A'
        else:
            return 'B'
    # make a code that will check if the guess is correct or wrong and will determine the next action based on the guess. 
    if guess.lower() == 'a':
        compare_followers(A,B)
        if compare_followers(A,B) == 'A':
            A = B
            high_score += 1
            print("Correct guess.")
            print(f"Your score {high_score}.")
            B = random.choice(data)
        else:
            print("Wrong guess. Game over.")
            print(f"Your score is {high_score}.")
            game = False
    elif guess.lower() == 'b':
        compare_followers(B,A)
        if compare_followers(B,A) == 'A':
            A = B
            high_score += 1
            print("Correct guess.")
            print(f"Your score {high_score}.")
            B = random.choice(data)
        else:
            print("Wrong guess. Game over.")
            print(f"Your score is {high_score}.")
            game = False  
    else:
        print("Wrong input. Try again.")






