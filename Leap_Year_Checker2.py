while True:    
    year = int(input("Which year do you want to check? "))
    div_4 = year / 4
    div_100 = year/ 100
    div_400 = year / 400
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            print("Leap Year.")
        elif year % 100 == 0 and year % 400 != 0:
            print("Not Leap Year.")
        else:
            print("Leap Year.")
    else:
        print("Not Leap Year.")
