import random
print("Welcome to the Rock, Paper, Scissors game!")
choices = ['Rock', 'Paper', 'Scissors']
choice = input("Pick a weapon:\nRock, Paper, Scissors ")
opponent = random.choice(choices)
print(f'You chose: {choice}')
print(f'I chose: {opponent}')

if choice.lower() == 'rock' and opponent == 'Rock':
    print("It's a tie")
elif choice.lower() == 'rock' and opponent == 'Paper':
    print('I win!')
elif choice.lower() == 'rock' and opponent == 'Scissors':
    print('You win!')

if choice.lower() == 'paper' and opponent == 'Paper':
    print("It's a tie")
elif choice.lower() == 'paper' and opponent == 'Scissors':
    print('I win!')
elif choice.lower() == 'paper' and opponent == 'Rock':
    print('You win!')

if choice.lower == 'scissors' and opponent == 'Scissors':
    print("It's a tie")
elif choice.lower == 'scissors' and opponent == 'Rock':
    print('I win!')
elif choice.lower == 'scissors' and opponent == 'Paper':
    print('You win!')
