#BMI CALCULATOR
print("Welcome to Jerome's BMI Calculator!")
while True:
    Name = input("What is your name? ")
    Weight = input("What is your weight (in kgs)? ")
    Height = input("What is your height(in m)?")

    BMI = float(Weight) / (float(Height) * float(Height))

    print("Your BMI is", BMI)
    if BMI < 18.5:
        print(Name, "You are underweight.")
    elif BMI < 25:
        print(Name, "You're normal.")
    elif BMI < 30:
        print(Name, "You're overweight.")
    else:
        print(Name, "You're obese.")
    ans = input('continue? (y/n):')
    if ans == 'n':
        print('OK have a nice day!')
        break
