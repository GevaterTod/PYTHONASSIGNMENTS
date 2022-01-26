print("ASSIGNMENT-1\nNAME-SUNPREET SINGH\nSID-21103118\n\n")

#Question 1
print("Question 1\n")

# (a)
# Take input as 'Python is a case sensitive language'

sInputString=input("Enter the statement: ")
print("(a) ",sInputString)
Length=len(sInputString)
print(Length)

# (b)

sReverseString=sInputString[Length::-1]
print("(b) ",sReverseString)

# (c)

NewString=sInputString[10:26]
print("c",NewString)

# (d)

#replace 'a case sensitive' with 'oject oriented'
ReplacedString=sInputString[0:10]+'object oriented'+sInputString[26:35]
print("(d)",ReplacedString)

# (e)

IndexA=sInputString.find('a')
print("(e)",IndexA)

# (f) first check the index of white spaces and then write the new string by not using those index

RemoveSpaces=sInputString.replace(" ","")
print("(f)",RemoveSpaces)


# Question 2
print("Question 2\n")
sName=input("Enter your name: ")
iSID=int(input("Enter your SID: "))
sDeptt=input("Enter your department name: ")
fCGPA=float(input("Enter your CGPA: "))
print('''Hey, %s Here!
My SID is %s
I am from %s department and my CGPA is %s'''%(sName,iSID,sDeptt,fCGPA))


# Question 3

print("\n\nQuestion 3\n")

#a=56 b=10
a=0b111000
b=0b1010

#(a)

print("(a)",bin(a&b))

#(b)

print("(b)",bin(a|b))

#(c)
print()
print("(c)",bin(a^b))

#(d)
print("(d)")
print(bin(a<<2))
print(bin(b<<2))

#(e)
print("(e)")
print(bin(a>>2))
print(bin(b>>4))


# Question 4
print("Question 4")

iNum1=int(input("Enter the first number:"))
iNum2=int(input("Enter the second number:"))
iNum3=int(input("Enter the third number:"))

if(iNum1>iNum2):
    if(iNum1>iNum3):
        print(iNum1,"is the greatest number")
    else:
        print(iNum3,"is the greatest number")
else:
    if(iNum2>iNum3):
        print(iNum2,"is the greatest number")
    else:
        print(iNum3,"is greatest number")


# Question 5
print("Question 5\n")

sUserInput=input("Give a word:")
if("name"in sUserInput):
    print("Yes\n")
else:
    print("No\n")


# Question 6
# Predicting whether a Triangle is possible whose sides are input by the user
print("Question 6")

iSide1=int(input("Give a number:"))
iSide2=int(input("Give a number:"))
iSide3=int(input("Give a number:"))

if(iSide1+iSide2>iSide3 and iSide2+iSide3>iSide1 and iSide1+iSide3>iSide2):
    print("The Given triangle is possible")
else:
    print("The Given triangle is not possible")