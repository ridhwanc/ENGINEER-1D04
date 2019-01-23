'''outfile=open('ridhwanissexy.txt','w')
outfile.write('I am learning how to create files')
outfile.close()'''

'''infile = open('ridhwanissexy.txt','r')
contents = infile.read()
print contents'''

#outfile=open('ridhwanissexy.txt','w')
#outfile.write('I am still learning how to create files fam')
#outfile.close()

#infile=open('ridhwanissexy.txt','r')
#contents = infile.read()
#print contents

import random

outfile=open('grades.txt','w')
for student in range(0,800):
    grade=random.randint(0,12)
    outfile.write(str(grade) +'\n')

outfile.close()

                  





            
