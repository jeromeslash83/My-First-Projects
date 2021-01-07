print("Welcome to Jerome's BMI Calculator!")
while True:
    Name = input("What is your name? ")
    Weight = input("What is your weight (in kgs)? ")
    Height = input("What is your height(in m)?")

    BMI = float(Weight) / (float(Height) * float(Height))

    print("Your BMI is", BMI)
    if BMI < 18.5:
        print(Name, "You are underweight.")
    elif BMI >= 18.5 or BMI == 24.9:
        print(Name, "You're normal.")
    elif BMI >=25.0 or BMI == 30.0:
        print(Name, "You're overweight.")
    else:
        print(Name, "You're obese.")
    ans = input('continue? (y/n):')
    if ans == 'n':
        break