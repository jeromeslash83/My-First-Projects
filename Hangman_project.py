word_list = ["aardvark", "baboon", "camel"]
import random
chosen_word = random.choice(word_list)
guess = input('Guess a letter from the given word: ')
if guess.lower() in chosen_word.lower:
  print('Yes') 
else:
  print('No')
