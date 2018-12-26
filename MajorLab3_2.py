def toHex(a):
    list1=[]
    for i in a:
        x = float.hex(i)
        list1.append(x)
    return list1

def toFloat(s):
    list2 = []
    for i in s:
        x = float.fromhex(i)
        list2.append(x)
    return list2

def encode(A,n):
    newlist = []
    newerlist = []
    newestlist = []
    for i in A:
        for j in i:
            x = j**n
            newlist.append(x)
        newerlist.append(newlist)
        newlist =[]

    for i in newerlist:
        y = toHex(i)
        newestlist.append(y)
        

def decode(S,n):
    newlist = []
    newerlist = []
    newestlist = []
    for i in S:
        x = toFloat(i)
        newlist.append(x)
    
    
    for i in newlist:
        for j in i:
            y = j**(1.0/n)
            newerlist.append(y)
        newestlist.append(newerlist)
        newerlist = []

    print newestlist
    
        
    
        
        


            
            

        

    
    
            
    

    
        
    
    
    

    
