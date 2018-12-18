# File: investment.py
# A simple program to calculate investments

def main():
    print("Welcome to Ridhwan's Investment Program")
    print("This program calculates the future value")
    print("of a 10 year investment.")

x = eval(input("Please enter the principal amount of your investment:" ))

apr = eval(input("Please enter the annual percentage rate:" ))

for i in range(10):
    x = x * (1+apr)

    print("The final value of your investment will be", x)

main()




