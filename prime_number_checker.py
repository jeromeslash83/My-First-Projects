#PRIME NUMBER CHECKER
while True:
    def prime_checker(number):
        for i in range (2, number-1):
            prime = True
            if number % i == 0:
                prime = False
        if prime:
            print("It's a prime number.")
        else:
            print("It's not a prime number.")
        

    n = int(input("Check this number: "))
    prime_checker(number=n)
