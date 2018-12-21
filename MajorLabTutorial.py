from Student import *

def createStudentList():
    f = raw_input(' enter file name' )
    infile = open(f,'r')
    lst = []

    for line in infile:
        name, num,c red, points = line.split('/t')
        st = Student(name, num, cred, points)
        lst.append(st)
    return lst

def highGPA(stList):
    higpa = stList[0].GPA()

    for st in stList:
        if st.GPA() > higpa:
            higpa = st.GPA()
        return higpa

def gpaStudentList(hiGPA, stList):
    lst = []
    for st in stList:
        if st.GPA() == hiGPA:
            lst.append(st)
    return lst

def main():
    stList - createStudentList()
    gpa = highGPA(stList)
    gpaList = gpaStudentList(gpa, stList)

    for st in gpaList:
        print st.getName(), st.getStNumber(), st.GPA()
    
