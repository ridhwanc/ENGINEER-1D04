''' Ridhwan Chowdhury
Major 3_1 Lab
GO HAM '''

def makeEdgeRow(w,c):
    return w*c

def makeRow(w,c):
    list1 = []
    for i in range(w):
        list1.append(' ')
    list1[0] = c
    list1[-1] = c
    x = ''.join(list1)
    return x

def makeBox(w,h,p):
    mainlist = []
    lst = list(p)

    for i in range(len(lst)):
        mainlist.append("")
        mainlist[0] = makeEdgeRow(w,lst[0])

    for i in range(1,(len(lst)-1)):
        mainlist[i] = makeRow(w, lst[i])

    x = len(mainlist)
    y = len(lst)

    mainlist[-1] = makeEdgeRow(w,lst[-1])

    print mainlist



        

    

    


    

    
        
    
