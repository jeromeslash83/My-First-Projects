print("Welcome to Jerome's tip calculator.")
while True:
    bill = input("What was the total bill? ")
    split = input("How many people will split the bill? ")
    tip = input("What percentage of tip would you like to give? (10, 12, or 15) ")
    bill_int = int(bill)
    split_int = int(split)
    tip_int = int(tip) / 100
    total = ((bill_int * tip_int) + bill_int) / split_int
    print("Your total bill for each person is:", total)
    continue_program = input("Do you want to make a calculation again? (Y/N) ")
    if continue_program.lower() == "N":
        break
