# Fizzbuzz!

#def fizz_buzz(input):
#    if input % 3 == 0:
      #  result = "Fizz"
  #  else
 #       result = "Buzz"

  #  return result

#If you wanted to be implemented better, you could remove the return
#And simply return the string wanted


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return  "Fizz"
    if input % 5 == 0:
        return "Buzz"
    
    return input


print(fizz_buzz(15))
        



        
     

    
