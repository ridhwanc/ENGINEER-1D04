#factorial.py
#Program is used to compute the factorial of any whole number
#Illustrates for loop with an accumlator (counter)

def main():
    n = input('Please enter a whole number: ')
    fact = 1
    for factor in range (n,1,-1):
        fact = fact * factor
        print ' The factorial of', n, 'is', fact
        
