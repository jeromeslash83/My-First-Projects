import random
print("Welcome to the Rock, Paper, Scissors game!")    
while True:    
    choice1 = input("Pick a weapon:\n0 for Rock, 1 for Paper, 2 for Scissors ")
    choice = int(choice1)
    opponent = random.randint(0,2)
    wee = ['Rock', 'Paper', 'Scissors']
    print(f'You chose: {wee[choice]}')
    print(f'I chose: {wee[opponent]}')
    you = 0
    opponent = 0
    if choice >= 3 or choice <0:
        print("Wrong number please try again")
    elif choice == 0 and opponent == 0:
        print("It's a tie")
        you += 1
        opponent += 1
    elif choice == 0 and opponent == 1:
        print('I win!')
        you += 0
        opponent += 1
    elif choice == 0 and opponent == 2:
        print('You win!')
        you += 1
        opponent += 0
    elif choice == 1 and opponent == 1:
        print("It's a tie")
        you += 1
        opponent += 1
    elif choice == 1 and opponent == 2:
        print('I win!')
        you += 0
        opponent += 1
    elif choice == 1 and opponent == 0:
        print('You win!')
        you += 1
        opponent += 1
    elif choice == 2 and opponent == 2:
        print("It's a tie")
        you += 1
        opponent += 1
    elif choice == 2 and opponent == 0:
        print('I win!')
        you += 0
        opponent += 1
    elif choice == 2 and opponent == 1:
        print('You win!')
        you += 1
        opponent += 0
    print(f'You: {you}\nYour opponent: {opponent}')

