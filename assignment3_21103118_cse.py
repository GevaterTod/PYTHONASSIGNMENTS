print("ASSIGNMENT-3\nNAME-SUNPREET SINGH\nSID-21103118\n\n")



# QUESTION 1

print("Question 1\n")

a=str(input("Enter A String: "))

list=a.split() 
dict={} 
if list.__len__()==1:   
    for i in list[0]:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)   
else:                   
    for i in list:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
print("\n")



# QUESTION 2
from subprocess import list2cmdline


print("Question 2\n")

def Next_Date():
    
    # List with 31 day Month
    List1=[1,3,5,7,8]
    # List with 30 day Month
    List2=[4,6,9,11]
    # List with 28 day Month
    List3=[2]
    
    List4=[12]
    while(True):                
        Day=int(input("Enter the day: "))
        if(1<=Day<=31):
            break
        else:
            print("Enter a valid day")
    while(True):                 
        Month=int(input("Enter Month: "))
        if(1<=Month<=12):
            break
        else:
            print("Enter a valid month")
    while(True):                 
        Year=int(input("Enter the Year: "))
        if(1800<=Year<=2025):
            break
        else:
            print("Please Enter Year from 1800 to 2025 only")
    if Month in List1 :    
        if(Day==31):
            Day=1
            Month=Month+1
            print(Day,"/",Month,"/",Year)
        elif(Day<31):
            Day+=1
            print(Day,"/",Month,"/",Year)
        else: 
            print("Date is invalid, Try again")
            Next_Date()
    
    elif Month in List2 :
        if(Day==30):
            Day=1
            Month=Month+1  
            print(Day,"/",Month,"/",Year)   
        elif(Day<30):
            Day+=1
            print(Day,"/",Month,"/",Year)
        else:
            print("Date is invalid, Try again") 
            Next_Date()      
    elif Month in List3:
        if(Year % 4 == 0):  
            if(Day==29):
                Day=1
                Month=Month+1
                print(Day,"/",Month,"/",Year)
            elif(Day<29):
                Day+=1
                print(Day,"/",Month,"/",Year)
            else:
                print("Date is invalid, Try again")
                Next_Date()
        else:
            if(Day==28):
                Day=1
                Month+=1
                print(Day,"/",Month,"/",Year)
            elif(Day<28):
                Day+=1
                print(Day,"/",Month,"/",Year)
            else:
                print("Date is invalid, Try again")
                Next_Date()
    elif Month in list4:
        if(Day==31):
            Day=1
            Month=1
            Year+=1  
            print(Day,"/",Month,"/",Year)
        elif(Day<31):
            Day+=1;
            print(Day,"/",Month,"/",Year)
        else:
            print("Date is invalid, Try again")
            Next_Date()
        
    else:
        print("Date is invalid, Try again")
        Next_Date()
Next_Date()
print("\n")



# QUESTION 3

print("Question 3\n")

InputList = input('Enter elements of the list separated by space ')

UserList = InputList.split()

print('List: ', InputList)

for i in range(len(UserList)):
    
    UserList[i] = int(UserList[i])
squarelist =[(UserList[i], UserList[i]**2) for i in range(len(UserList))]

print(squarelist)

print("\n")


# QUESTION 4

print("Question 4\n")

def InputPoint():
    Point = int(input("Enter Grade Point: "))
   
    if Point>10 or Point<4:
        print("Invalid grade point! Try Again")
        Point = InputPoint()
    return Point
Grade=InputPoint()

if(Grade==4): print("Your Grade is 'D' and Poor Performance")
elif(Grade==5): print("Your Grade is 'C' and Below Average Performance")
elif(Grade==6): print("Your Grade is 'C+' and Average Performance")
elif(Grade==7): print("Your Grade is 'B' and Good Performance")
elif(Grade==8): print("Your Grade is 'B+' and Very Good Performance")
elif(Grade==9): print("Your Grade is 'A' and Excellent Performance")
elif(Grade==10): print("Your Grade is 'A+' and Outstanding Performance")
print("\n")


# QUESTION 5 

print("Question 5\n")

a=6
for i in range(a):
    # printing spaces
    for j in range(i):
        print(' ', end='')
    for j in range(2*(a-i)-1):
        print(chr(65 + j), end='')
print("\n")

# QUESTION 6

print("Question 6\n")

SID = int(input("Enter the SID: "))
Name = input("Enter the Name: ")
Students = {SID:Name}

while True:
    Option = input("Do you want another student entry (Y for Yes, N for No):").upper()
    if Option == 'Y':
        SID = int(input("Enter SID: "))
        Name = input("Enter Name: ")
        Students[SID] = Name
    elif Option == 'N':
        break
    else:
        print('Input is Invalid!')

# (a)
print("(a)",Students)

# (b)
print("(b)",{k:v for k,v in sorted(Students.items(), key= lambda x:x[1])})

# (c)

print("(c)",{k:v for k,v in sorted(Students.items())})

# (d)

SID = int(input("Search Name with SID: "))
print("(d)",Students[SID])

print("\n")


# QUESTION 7
print("Question 7\n")

def FiboRecur(n):
   if n <= 1:
       return n
   else:
       return(FiboRecur(n-1) + FiboRecur(n-2))
NoOfTerms=int(input("Enter the no. of terms: "))
if NoOfTerms <= 0:    
    # Enter the fibonacci sequence
   print("Enter a positive integer")
else:
   print("Fibonacci sequence:")
   sum=0
   for i in range(NoOfTerms):
       print(FiboRecur(i))
       sum=sum+FiboRecur(i)
AvgFibo=float(sum/NoOfTerms)
print("Avg Resultant of Fibonacci series:",AvgFibo)
print("\n")


# QUESTION 8

print("Question 8\n")

Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}

# (a)
SetUnion = Set1.union(Set2)
SetIntersection = Set1.intersection(Set2)
PartASet = SetUnion - SetIntersection
print("(a) ", PartASet)

# (b)
PartBSet = Set1.union(Set2.union(Set3)) - Set1.intersection(Set2) - Set2.intersection(Set3) - Set3.intersection(Set1)
print("(b) ", PartBSet)

# (c)
PartCSet=((Set1.intersection(Set2)).union((Set1.intersection(Set3)).union(Set2.intersection(Set3))))-(Set1.intersection(Set2.intersection(Set3)))
print("(c) ",PartCSet)

# (d)
PartDSet = set()
for i in range(1, 11):
    if i not in Set1:
        PartDSet.add(i)
print("(d) ", PartDSet)

# (e)
PartESet = set()
for i in range(1, 11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        PartESet.add(i)
print("(e) ", PartESet)