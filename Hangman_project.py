#HANGMAN GAME
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')

display = []
for n in chosen_word:
    display.append('_')
print(display)
guess = input("Guess a letter: ").lower()
number = int(len(chosen_word))

for n in range(number) :
    letter = chosen_word[n]
    if letter == guess:
         display[n] = guess
print(display)
