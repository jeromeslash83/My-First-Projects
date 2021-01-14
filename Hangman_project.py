word_list = ["aardvark", "baboon", "camel"]
import random
chosen_word = random.choice(word_list)
guess = input('Guess a letter from the given word: ')
numbers = int(len(chosen_word))
for n in range(0, numbers):
    if guess.lower() in chosen_word.lower()[n]:
        print('Yes') 
    else:
        print('No')
