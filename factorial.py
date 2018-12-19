#factorial.py
#  Program to compyte ethe factorial of a number
# Illustrates for loop with an accumlator

def main():
    n = input('Please enter a whole number: ')
    fact = 1
    for factor in range (n,1,-1):
        fact = fact * factor
        print ' The factorial of', n, 'is', fact
        
