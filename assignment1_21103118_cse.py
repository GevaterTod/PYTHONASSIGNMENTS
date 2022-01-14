print("ASSIGNMENT-1\nNAME-SUNPREET SINGH\nSID-21103118\n\n")


# QUESTION 1
print("Question 1\n")

#Python Program for finding average of three numbers

iFirstNo=input("Enter first number\n")
iSecondNo=input("Enter second number\n")
iThirdNo=input("Enter third number\n")

#Average of three numbers
fAvg=(int(iFirstNo)+int(iSecondNo)+int(iThirdNo))/3
print("The average of three numbers is :")
print(fAvg)


# Question 2
print("\n\nQuestion 2\n")

# Computing tax payable by the user

# Standard Deduction= $10000
iStdDed=10000
# Dependent Deduction per Dependent= $3000
iDependDed=3000
# No. of Dependents
iDependNo=input("Enter the Number of Dependents\n")
# Total Dependent Deduction= Dependent Deduction per Dependent * No.of dependents
# And declaring No. of Dependents as int variable
iTotalDependDed=iDependDed*int(iDependNo)

# Gross Income of the user
iGrossIncome=input("Enter your Gross Income\n")

# Total Taxable Income= Gross Income - (Standard Deduction + Total Dependent Deduction)
iTaxableIncome=int(iGrossIncome)-int(iStdDed)-int(iTotalDependDed)

# Tax rate= 20%
# Total Tax Payable= Taxable Income * 20%
iTax=(float((iTaxableIncome)*20)/100)
print("Total Tax Payable =",iTax)




# Question 3
print("\n\nQuestion 3\n")

# Storing Student Credentials

iSID=int(input("Enter your SID\n"))
sName=input("Enter your name\n")
# Input of M,F,U for Male,Female and Unknown respectively
sGender=input("For Gender\nEnter M,F,U for Male,Female and Unknown respectively\n")
sCourseName=input("Enter your Course Name\n")
fCGPA=float(input("Enter your CGPA\n"))

#Creating list to get the student credentials
indStudentCred=[iSID,sName,sGender,sCourseName,fCGPA]

# Printing Student Credentials
print(indStudentCred)


# Question 4
print("\n\nQuestion 4\n")

# Sorting entered marks of 5 students

# Getting input of marks of 5 students from the user
iStudent1=input("Enter marks of Student 1\n")
iStudent2=input("Enter marks of Student 2\n")
iStudent3=input("Enter marks of Student 3\n")     
iStudent4=input("Enter marks of Student 4\n")
iStudent5=input("Enter marks of Student 5\n")

# Creating a list of the marks
indSortMarks=[iStudent1,iStudent2,iStudent3,iStudent4,iStudent5]

# Sorting marks of the 5 students
indSortMarks.sort()

print(indSortMarks)

# Question 5
print("\n\nQuestion 5\n")

# Creating list of 6 colors; Red, Green, White, Black, Pink, Yellow
indColor=['Red','Green','White','Black','Pink','Yellow']

# Removing 4th element i.e. Black from the list 
indColor.remove(indColor[3])
print("a.",indColor)

indColor=['Red','Green','White','Black','Pink','Yellow']
# Removing Black and Pink from the list and replacing them with Purple
indColor[3:5]=['Purple']
print("\nb.",indColor)