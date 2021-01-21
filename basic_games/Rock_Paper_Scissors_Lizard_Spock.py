import random
print("Welcome to the World of Rock, Paper, Scissors, Spock")
while True:
    jan_ken_pon = ["Rock","Paper","Scissors","Lizard","Spock"]
    randomize = random.choice(jan_ken_pon)
    play = input("Do you want to play? (Y/N)\n")
    if play.lower() == "n":
        break
    choice = input("Pick your choice:\n Rock, Paper, Scissors, Lizard, Spock\n")
    print(f"You chose: {choice}.\nI chose {randomize}.")
    if choice.lower() == "scissors" and randomize == "Scissors":
        print("It's a tie, one more time!")
    elif choice.lower() == "scissors" and randomize == "Rock":
        print("Haha, I win, better luck next time!")
    elif choice.lower() == "scissors" and randomize == "Spock":
        print("Haha, I win, better luck next time!")
    elif choice.lower() == "scissors" and randomize == "Paper":
        print("You win. One more time!")
    elif choice.lower() == "scissors" and randomize == "Lizard":
        print("You win. One more time!")
    elif choice.lower() == "rock" and randomize == "Paper":
        print("Haha, I win, better luck next time!")  
    elif choice.lower() == "rock" and randomize == "Spock":
        print("Haha, I win, better luck next time!")  
    elif choice.lower() == "rock" and randomize == "Rock":
        print("It's a tie. One more time!")
    elif choice.lower() == "rock" and randomize == "Lizard":
        print("You win. One more time!")
    elif choice.lower() == "rock" and randomize == "Scissors":
        print("You win. One more time!")
    elif choice.lower() == "paper" and randomize == "Rock":
        print("You win. One more time!")
    elif choice.lower() == "paper" and randomize == "Spock":
        print("You win. One more time!")
    elif choice.lower() == "paper" and randomize == "Paper":
        print("It's a tie. One more time!")
    elif choice.lower() == "paper" and randomize == "Scissors":
        print("Haha, I win, better luck next time!")
    elif choice.lower() == "paper" and randomize == "Lizard":
        print("Haha, I win, better luck next time!")
    elif choice.lower() == "spock" and randomize == "Lizard":
        print("Haha, I win, better luck next time!")
    elif choice.lower() == "spock" and randomize == "Paper":
        print("Haha, I win, better luck next time!")
    elif choice.lower() == "spock" and randomize == "Spock":
        print("It's a tie. One more time!")
    elif choice.lower() == "spock" and randomize == "Rock":
        print("You win. One more time!")
    elif choice.lower() == "spock" and randomize == "Scissors":
        print("You win. One more time!")
    elif choice.lower() == "lizard" and randomize == "Scissors":
        print("Haha, I win, better luck next time!")
    elif choice.lower() == "lizard" and randomize == "Rock":
        print("Haha, I win, better luck next time!")
    elif choice.lower() == "lizard" and randomize == "Lizard":
        print("It's a tie. One more time!")
    elif choice.lower() == "lizard" and randomize == "Paper":
        print("You win. One more time!")
    elif choice.lower() == "lizard" and randomize == "Spock":
        print("You win. One more time!")

