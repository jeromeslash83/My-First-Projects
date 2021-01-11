import random
print("Welcome to the Rock, Paper, Scissors game!")
choice1 = input("Pick a weapon:\n0 for Rock, 1 for Paper, 2 for Scissors ")
choice = int(choice1)
opponent = random.randint(0,2)
print(f'You chose: {choice}')
print(f'I chose: {opponent}')
if choice >2 or <0:
    print("Wrong number please try again")
elif choice == 0 and opponent == 0:
    print("It's a tie")
elif choice == 0 and opponent == 1:
    print('I win!')
elif choice == 0 and opponent == 2:
    print('You win!')
elif choice == 1 and opponent == 1:
    print("It's a tie")
elif choice == 1 and opponent == 2:
    print('I win!')
elif choice == 1 and opponent == 0:
    print('You win!')
elif choice == 2 and opponent == 2:
    print("It's a tie")
elif choice == 2 and opponent == 0:
    print('I win!')
elif choice == 2 and opponent == 1:
    print('You win!')

