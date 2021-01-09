print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island!\nYour mission is to find the treasure")
fork = input("You've reached a fork in the road. Which way will you go to? (Right or Left)\n")
if fork.lower() == "left":
    print("You have found a passageway that leads you to the river")
    river = input("You've reached the river. What will you do?\n(Swim/Wait)")
    if river.lower() == "wait":
        print("A boat picks you up.")
        island = input("You've reaced the final destination. There are three doors to choose from which one will you choose\n(Blue, Red, or Yellow) ")
        if island.lower() == "yellow":
            print("You Win!")
        elif island.lower() == "blue":
            print("A dragon kills you. Game over.")
        elif island.lower() == "red":
            print("A black hole swallows you. Game over.")
        else:
            print("Wrong input. You're hit by lightning. Game over.")
    elif river.lower() == "swim":
        print("Piranhas eat you. Game over")
    else :
        print("Wrong input. Monsters kill you. Game over")
elif fork.lower() == "right":
    print("You fell into the abyss. Game over.")
else:
    print("Wrong input. A monster kills you. Game over.")