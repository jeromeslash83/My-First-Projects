while True:    
    year = int(input("Which year do you want to check? "))
    div_4 = year / 4
    div_100 = year/ 100
    div_400 = year / 400
    if div_4 - int(div_4) == 0:
        if div_100 - int(div_100) == 0 and div_400 - int(div_400) == 0:
            print("Leap Year.")
        elif div_100 - int(div_100) == 0 and div_400 - int(div_400) != 0:
            print("Not Leap Year.")
        else:
            print("Leap Year.")
    else:
        print("Not Leap Year.")
