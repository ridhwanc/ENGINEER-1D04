# Reverse a string

inputStr = 'RidhwanIsASav'

#initialize an empty string
result = ''

#run a loop from len(inputStr)-1 to 0
#within the loop, append characters from the end of the string to the beginning into the result string

for i in range(len(inputStr)-1,-1,-1):
    result = result + inputStr[i]


#print reversed string

print(result)
