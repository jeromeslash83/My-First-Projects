print("Welcome to the rollercoaster!")
height = input("How tall are you? cm: ")
bill = 0
if int(height) > 120:
    age = input("How old are you? ")
    if int(age) <= 5:
        bill = 3
    elif int(age) <= 18:
        bill = 5
    else :
        bill = 7

    photo = input("Do you want a photo taken? (Y/N) ")
    if photo.lower() == "y":
        bill += 5
        
    print(f"Your bill is ${bill}.")
else:
    print("You're not allowed to ride the rollercoaster.")
