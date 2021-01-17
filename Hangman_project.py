#HANGMAN GAME
import random
print('Welcome to HANGMAN')
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

display = []
for n in chosen_word:
    display.append('_')
print(display)
lives = []
loser = 'HANGMAN'
win = 0
lose = 0
number = int(len(chosen_word))
while win != number:
    guess = input("Guess a letter: ").lower()
    for n in range(number) :
        letter = chosen_word[n]
        if letter == guess:
            display[n] = guess
            win += 1
    if not guess in chosen_word:
        lose += 1
        for i in range(1,8):
            if lose == i:
                lives.append(loser[i-1])
    
    if lose == 7:
        print('You Lose.')
        break
    print(f'Correct answer:\n{display}\n\n')
    print(f'Lives:\n{lives}\n')
else:
    if win == number:
        print('You Win.')
