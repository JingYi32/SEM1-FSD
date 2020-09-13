'''
#WAP to print Hello 10 times.
print ("To Hello 10 times.")
#WHILE LOOP
no = 1
while (no<=10):
    print (no, "Hello")
    no = no + 1
    
#FOR LOOP with 1 value in range
print ("\n")
for no in range (10):
    print (no, "FOR Hello")
    
#FOR LOOP with 2 values in range
print ("\n")
for no in range (1,11):
    print (no, "2nd for Hello")
    
#FOR LOOP with 3 values in range
print ("\n")
for no in range (1, 11, 1):
    print (no, "3nd for Hello")



#Q2:WAP to numbers from 1 to 20 and display addition of all numbers at the end.
print ("\n\n\nQ2.Print numbers from 1 to 20.")
#WHILE LOOP
no = 1
add = 0
while (no <= 20):
    print (no)
    add = add + no
    no = no + 1
print ("Addition of these numbers is ",add, ".")

#FOR LOOP
print ("\n")
add = 0
for no in range (1,21):
    print ("FOR",no)
    add = add + no
print ("Addition of these numbers is ",add,".")



#Q5: WAP and draw a flowchart to accept number from user and print Time Table of given number in following format.
#While loop
no = int (input ("\n\n\nQ5.Enter a value to print Time Table of given number: "))
cnt = 1
while (cnt <= 10):
    mult = no * cnt
    print (no, "X", cnt, "\t=", mult)
    cnt = cnt + 1
    
#For LOOP
no = int (input ("\nLOOP Enter a value to print Time Table of given number: "))
for cnt in range (1,11):
    mult = no * cnt
    print ("FOR", no, "X", cnt, "\t=", mult)



#Q3: WAP to print all EVEN numbers from 1 to 20.
print ("\n\n\nQ3.All Even numbers from 1 to 20.")
#While Loop
no = 1
while (no<=20):
    if (no%2 == 0):
        print (no)
    no = no + 1

#FOR LOOP
print ("\n")
no = 1
for no in range (1,21):
     if (no%2 == 0):
         print ("FOR",no)



#Q4: WAP to print all EVEN and ODD numbers from 1 to 20.
print ("\n\n\nQ4.EVEN numbers and ODD numbers from 1 to 20.")
#while loop
print ("ODD \t EVEN")
no = 1
while (no<=20):
    if (no%2 == 0):
        print (no-1,"\t",no)

    no = no + 1
    
#FOR LOOP
print ("\nLOOP\nOdd\t","Even")
for x in range(1,21):
    if x%2==0:
        print(x-1,"\t",x)



#Q6: WAP to print all EVEN and ODD numbers from 1 to 20. Also display all EVENSUM and ODDSUM at the end.
print("\n\n\nQ6.EVEN numbers and ODD numbers from 1 to 20 and EVENSUM & ODDSUM.")
#WHILE LOOP
print ("Even \t ODD")
no = 1
ES = 0
OS = 0
while (no<=20):
    if (no%2 == 0):
        print (no)
        ES = ES + no
    else:
        print ("\t",no)
        OS = OS + no
    no = no + 1
print("\nOddSUM from 1 to 20 is :",OS,
      "\nEvenSUM from 1 to 20 is:",ES)

#FOR LOOP
no = 1
ES = 0
OS = 0
for no in range(1,21):
    if (no%2==0):
        print (no)
        ES = ES + no
    else:
        print ("\t",no)
        OS = OS + no
print("\nOddSUM from 1 to 20 is :",OS,
      "\nEvenSUM from 1 to 20 is:",ES)



#Q7: WAP to find factorial of a given number.
#WHILE LOOP
no = int (input ("\n\n\nQ7.Enter a value to find factorial of a given number:"))
fact = 1
while (no>0):
    fact = fact * no
    no = no - 1
print( "Factorial is",fact)

#FOR LOOP
no = int (input ("FOR Enter a value to find factorial of a given number:"))
fact = 1
for no in range (no, 0, -1):
    fact = fact * no
print( "FOR Factorial is",fact)
'''


#Q8: WAP to find reverse of a given number.
#WHILE LOOP
no = int (input("\n\n\nQ8.Enter a value to find reverse of a given number: "))
rev = 0
while (no > 0):
    rem = no % 10
    rev = (rev *10) + rem
    no = no//10
print ("The reverse of the given number is:",rev)

#FOR LOOP
no = int (input("\n\n\nLOOPQ8.Enter a value to find reverse of a given number: "))
rev = 0
for no in range (0, 4, no//10):
    rem = no % 10
    rev = (rev *10) + rem
print ("The reverse of the given number is:",rev)


'''
#10:WAP to check given number is Palindrome or not.
#WHILE LOOP
no = int (input("\n\n\nQ10.Enter a value to check given number is Palindrome or not: "))
check = no
rev = 0
while (no > 0):
    rem = no % 10
    rev = (rev *10) + rem
    no = no//10
if (rev == check):
    print ("Yes, the given number is a Palindrome.")
else:
    print ("No, the given number is not a Palindrome.")
    
#FOR LOOP
no = int (input("Enter a value to check given number is Palindrome or not: "))
check = no
rev = 0



#12:WAP to print SUM-OF-DIGIT of a given number.
#WHILE LOOP
no = int (input ("\n\n\nQ12.Enter a value to print SUM-OF-DIGIT of a given number: "))
add = 0
while (no > 0):
    rem = no % 10
    add = add + rem
    no = no // 10
print ("The sum of digit of the given number is", add, ".")

#FOR LOOP
no = int (input ("LOOP Enter a value to print SUM-OF-DIGIT of a given number: "))
add = 0



#Q9. WAP to check given number is ARMSTRONG number or not.
#WHILE LOOP
no = int (input ("\n\n\nQ9.Enter a value to check given number is ARMSTRONG number or not: "))
check = no
temp = 0
add = 0
while (no>0):
    rem = no % 10
    temp = rem * rem * rem
    add = temp + add
    no = no // 10
if (check == add):
    print ("Yes, the given number is an Armstrong number.")
else:
    print ("No, the given number is not an Armstrong number.")
    
#FOR LOOP
no = int (input ("\n\n\nEnter a value to check given number is ARMSTRONG number or not: "))
check = no
temp = 0
add = 0



#Q11. WAP to find the Fibonacci Series up to 10.
print ("\n\n\nQ11.Fibonacci Series up to 10.")
#WHILE LOOP
A = 0
B = 1
cnt = 1
print (A)
print (B)
while (cnt <= 10):
    C = A + B
    print (C)
    A = B
    B = C
    cnt = cnt + 1

#FOR LOOP
print ("\n")
A = 0
B = 1
cnt = 1
print (A)
print (B)
for cnt in range (1, 11):
    C = A + B
    print (C)
    A = B
    B = C    



#Q13. WAP to check given number is Prime number or not.
no = int (input ("\n\n\nQ13.Enter a value to check given number is Prime number or not: "))
cnt = 2
flag = 0
while (cnt < no):
    if (no%cnt == 0):
        flag = 1
        break
    cnt = cnt + 1
if (flag == 0):
    print ("Yes, the given number is a prime number.")
else:
    print ("No, the given number is not a prime number.")
    
#LOOP STRUCTURE
no = int (input ("LOOP Enter a value to check given number is Prime number or not: "))
cnt = 2
flag = 0
for cnt in range (2,no):
    if (no%cnt == 0):
        flag = 1
        break
    cnt = cnt + 1
if (flag == 0):
    print ("Yes, the given number is a prime number.")
else:
    print ("No, the given number is not a prime number.")

'''
