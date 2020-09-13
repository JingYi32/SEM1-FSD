
#Q1. WAP to print ‘Hello’.
print("Q1. WAP to print ‘Hello’.")
print ("Hello")

#Q2. WAP to accept value in program & display it.
print("\n\n\nQ2. WAP to accept value in program & display it.")
no=10
print("Your value is: ",no, ".")

#Q3. WAP to accept value from user & display it.
print("\n\n\nQ3. WAP to accept value from user & display it.")
no1 = int(input("Enter your value here: "))
print("Your entered value is",no1,".\n")

no2 = float(input("Enter your value here: "))
print("Your entered value is",no2, ".\n")

name = str(input("Enter your name\t: "))
print("Your name is",name,".")

#int is for integer number
#float is for decimal number
#str is for word


#Q4. WAP to accept 2 numbers from users and display addition of it.
print("\n\n\nQ4. WAP to accept 2 numbers from users and display addition of it.")
no1 = int (input("Enter first value here\t: "))
no2 = int (input("Enter second value here\t: "))
add = no1 + no2
print("Addition of the two numbers is: ",add,".")

#Q5. WAP to accept 2 input values from user and do an arithmetic operation (+, -, *, /, %,//,**).
print("\n\n\nQ5. WAP to accept 2 input values from user and do an arithmetic operation (+, -, *, /, %,//,**).")
no1 = int (input("Enter first value here\t: "))
no2 = int (input("Enter second value here\t: "))
add = no1 + no2
sub = no1 - no2
mul = no1 * no2
div = no1/ no2
mod = no1 % no2
divint = no1//no2
power = no1 ** no2
print("\nThe arithmetic operation of these two number is:"
      "\n\tAddition\t\t:",add,
      "\n\tSubtraction\t\t:",sub,
      "\n\tMultiplication\t\t:",mul,
      "\n\tDivision\t\t:",round(div,2),
      "\n\tModulus\t\t\t:",mod,
      "\n\tDivision with integer\t:",divint,
      "\n\tPower\t\t\t:",power)


#Q6. WAP to accept 2 values from user and print swapping of those number.
print("\n\n\nQ6. WAP to accept 2 values from user and print swapping of those number.")
no1 = int (input("Enter first value here\t: "))
no2 = int (input("Enter second value here\t: "))
print ("Before swapping values, the first number is",no1, "and the second number is",no2,".")
TEMP = no1
no1 = no2
no2 = TEMP
print("After swapping values, the first number is",no1, "and the second number is",no2, ".")

#Q7. WAP to calculate the area and the circumference for a circle.
print("\n\n\nQ7. WAP to calculate the area and the circumference for a circle.")
R = int(input("Enter the radius of circle in centimeter:"))
P = 3.142
A = P * R *R
C = 2 * P *R
print("The area of the circle is",round(A,3),"cm and the circumference is",round(C,3),"cm.")

#Q8. WAP to accept 5 subject marks from student and calculate the total and percentage (average) of a student for a semester and display it.
print("\n\n\nQ8. WAP to accept 5 subject marks from student and calculate the total and percentage (average) of a student for a semester and display it.")

a = int (input("Enter your 1st subject mark:"))
b = int (input("Enter your 2nd subject mark:"))
c = int (input("Enter your 3rd subject mark:"))
d = int (input("Enter your 4th subject mark:"))
e = int (input("Enter your 5th subject mark:"))

TOTAL = a+b+c+d+e
AVE = TOTAL / 5

print("Total of the semester is",TOTAL,"%" " and the Percentage is",round(AVE,4), "% .")


#Q9. WAP to accept Basic from an employee and calculate salary of an employee by considering following things. (Grade pay is double of Basic. DA is 70% of Basic. TA is RM 200. HRA is 20% of Basic.) (Formula for salary = Grade pay + DA + TA + HRA).
print("\n\n\nQ9. WAP to accept Basic from an employee and calculate salary of an employee.")

BSC = int(input ("Enter the basic: RM"))
GP = BSC + BSC
DA = BSC * 0.7
TA = 200
HRA = BSC * 0.2
SLY = GP + DA + TA + HRA
print("The total salary of the employee is RM",SLY, ".")
