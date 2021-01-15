word_list = ["aardvark", "baboon", "camel"]
import random
chosen_word = random.choice(word_list)
number = in(len(chosen_word))
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
  else:
print(display)
