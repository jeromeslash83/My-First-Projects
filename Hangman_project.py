word_list = ["aardvark", "baboon", "camel"]
import random
chosen_word = random.choice(word_list)
guess = input('Guess a letter from the given word: ')
for letter in chosen_word:
    if letter == guess:
        print('Yes')
    else :
        print('No')
