print("ASSIGNMENT-4\nNAME-SUNPREET SINGH\nSID-21103118\n\n")


# QUESTION 1

print("Question 1\n")

def TowerOfHanoi(n , fromRod, toRod, midRod):
	if n == 0:
		return
	TowerOfHanoi(n-1, fromRod, midRod, toRod)
	print("Move disk",n,"from rod",fromRod,"to rod",toRod)
	TowerOfHanoi(n-1, midRod, toRod, fromRod)
n = 3
TowerOfHanoi(n, 'A', 'C', 'B')

print("\n")


# QUESTION 2

print("Question 2\n")

from math import factorial, remainder

from tracemalloc import start

n=int(input('Enter the rows of pascals triangle '))

print("Using Loops")

for i in range(n):
	for j in range(n-i+1):
		print(end=" ")

	for j in range(i+1):
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")	
	print()
print("\n\n")

print("Using Recursion")

def PascalTriangle(n,origLength=n):
    if n == 0:
        return
    PascalTriangle(n-1,origLength)
  
    print('  '*(origLength-n), end='')

    start = 1
    for i in range(1, n+1):

        print(start, end ='   ')
     
        start = start * (n - i) // i
    print()

PascalTriangle(n)

print("\n")


# QUESTION 3 

print("Question 3\n")

Int1, Int2 = map(int,input("Enter 2 numbers: ").split())
Quotient = Int1 // Int2
Remainder = Int1 % Int2

# (a)

print("(a) Checking if the quotient and remainder is a callable value or not.")
print(callable(Quotient))
print(callable(Remainder))

# (b)

if (Quotient == 0):
    print("(b) The quotient is zero")
if (Remainder == 0):
    print("(b) The reminder is zero")
if (Quotient != 0 and Remainder != 0):
    print("(b) All the values are non zero")

# (c)

partClist = [Quotient + 4, Remainder + 4, Remainder + 5, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]

result = []
for i in range(len(partClist)):
    if partClist[i] > 4:
        result.append(partClist[i])
print(f"(c) Filtered out numbers that are greater than 4 are : {result}")

# (d)

setresult = set(result)
print("(d) Set:",setresult)

# (e)

immutableSet = frozenset(setresult) 
print("(e) Immutable Set:",immutableSet)

# (f)

print("(f) Hash value of maximum of set:", hash(max(immutableSet)))

print("\n")


# QUESTION 4

print("Question 4\n")

class Student:
    def __init__(self, student,roll_no):
        self.name = student
        self.roll_no = roll_no
    
    def __del__(self):
        print("Object deleted")

Student1 = Student("Sunpreet Singh", 21103118)
print("Object created")

print("The name of the student is {Student1.name} and SID is {Student1.roll_no}.")

del Student1

print("\n")


#QUESTION 5

print("Question 5\n")

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 

Employee1 = Employee("Mehak", 40000)
Employee2 = Employee("Ashok", 50000)
Employee3 = Employee("Viren", 60000)

Employee1.salary = 70000

# (a)
print("(a) The updated salary of {Employee1.name} is {Employee1.salary} ")

# (b)
print("(b)Record of Viren deleted", end='')
del Employee3

print("\n")


#QUESTION 6

print("Question 6\n")

Word =input("Enter word: ")
Word=Word.lower()

test_word = input("Enter New Meaningful Word using same letters to test friendship: ")
test_word=test_word.lower()

def count_in_dict(Word):
    count = {}
    list1 = list(Word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count

def userinput():
    if count_in_dict(Word) != count_in_dict(test_word):
        print("The letters are not same, Friendship is fake")
        return
    ans = input("Does word makes sense?(Y or N)")

    if ans=='Y':
        print("The friends pass this Friendship Test")
    elif ans=='N':
        print("This word doesn't have meaning, Friendship is fake")
    else:
        print("Invalid Input,try again with Y or N ")
        userinput()
userinput()