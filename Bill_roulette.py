import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
x = len(names)
y = random.randint(0, x - 1)
z = names[y]
print(f"{z} will pay all the bills!")
