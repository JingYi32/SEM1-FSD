'''
#WAP to accept 2 values from user and display the additition
def addition():
    add = no1 + no2
    print ("Addition is:",add)

no1 = int (input("Enter first value:"))
no2 = int (input("Enter second value:"))
addition()

#WAP to accept 2 values from user and display output for all
#arithmetic operations (+,-,*,/). for each opeartion use different function.

def addition():                 #fuction without parameter
    add = no1 + no2
    print ("Addition\t:",add)

def subtraction(no1,no2):       #function with parameters
    sub = no1 - no2
    print ("Subtraction\t:",sub)

def multiplication(a,b):
    mult = a * b
    print ("Multiplication\t:",mult)
    
def division(x,y):              #value return function
    div = x / y
    return div

no1 = int (input("Enter first value:"))
no2 = int (input("Enter second value:"))

addition()
subtraction(no1,no2)
multiplication(no1,no2)
result = division (no1,no2)
print ("Division\t:",round(result,2))
print (div)

#WAP
#
def addition():
    add = no1 + no2
    print ("Addition\t:",add)

def subtraction(no1,no2):
    sub = no1 - no2
    print ("Subtraction\t:",sub)

def multiplication(a,b):
    mult = a * b
    print ("Multiplication\t:",mult)
    
def division(x,y):
    div = x / y
    return div

ans = input ("Enter any key to continue and '1' to terminate:")
while (ans != '1'):
    no1 = int (input("Enter first value:"))
    no2 = int (input("Enter second value:"))
    print ("Arithmetic Operations are:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
    option = int (input("Enter your option:"))
    if (option == 1):
        addition()
    elif (option == 2):
        subtraction(no1,no2)
    elif (option == 3):
        multiplication(no1,no2)
    elif (option == 4):
        result = division (no1,no2)
        print ("Division\t:",round(result,2))
    else:
        print ("Wrong option. Good Bye.")
    ans = input ("Enter any key to continue and '1' to terminate:")

#WAP to create a list numbers using these number = 65, 75, 85, 95, 105 and define a function  check_number that prompt the user to enter a number to check that number is available or not in list.
def func():
    if no in mylist:
        print ("The number is available in the list.")
    else:
        print ("The number is not available in the list.")
mylist = [65,75,85,95,105]
no = int(input("Enter a value to check the number is available in list or not:"))
func()'''

#Q8.WAP to read name of student, TP Number and enter his/her all subject marks in list. Compute the total and percentage (Average) of a student. At the end display Name of student, TP Number, Total, Percentage and Grade of that semester by using function as defined below.
#(Note: 100-80 = A+          80-75 = A             75-70 = B+           70-65 = B             65-60 = C+            60-55 = C             55-50 = C-            50-0 = D/Fail).
#Use Display function to print output.
#Use mark function to accept parameter and return total to Display function.
#Use average function by passing parameter which is generated in mark function.
#Use grade function by passing parameter which is generated in average function.

def display_f():
    name = input ("Enter student name\t:")
    tp = int (input("Enter student TP number\t: TP"))
    sub = int (input("Enter total subjects in this semester:"))

    TOTAL = mark_f(sub)
    AVE = ave_f(TOTAL,sub)
    GRADE = grade_f(AVE)
    print ("\n\n\tWelcone to APU Grade System\n\tHere is your result")
    print ("Student Name\t\t\t:",name,"\nStudent TP number\t\t: TP",tp, "\nTotal mark of this semester\t:",TOTAL, "\nPercentage of this semester\t:",AVE,"\nGrade\t\t\t\t:",GRADE)

def mark_f(limit):
    mark_list=[]
    no = 1
    for mark in range (0,limit):
        print ("Enter mark of subjuct",no, ":")
        mark = int(input())
        if (mark <=100 and mark >=0):
            mark_list.append(mark)
        else:
            print ("Kindly insert the mark again")
            print ("Enter mark of subjuct",no, ":")
            mark = int(input())
        no = no + 1
    total = 0
    for mark in mark_list:
        total = total + mark
    return total

def ave_f(total, sub):
    ave = int (total / sub)
    return ave

def grade_f(ave):
    if (ave <= 100 and ave >= 80):
        grade = "A+"
    elif (ave < 80 and ave >= 75):
        grade = "A"
    elif (ave < 75 and ave >= 70):
        grade = "B+"
    elif (ave < 70 and ave >= 65):
        grade = "B"
    elif (ave < 65 and ave >= 60):
        grade = "C+"
    elif (ave < 60 and ave >= 55):
        grade = "C"
    elif (ave < 55 and ave >= 50):
        grade = "C-"
    else:
        grade = "D (Fail)"
    return grade

def option():
    ans = input("Do you want to continue. '0' to continue, '-1' to Terminate:")
    while (ans == '0'):
        display_f()
        ans = input("Do you want to continue. '0' to continue, '-1' to Terminate:")
    print ("GOOD BYE")

option()
