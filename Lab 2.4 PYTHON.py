'''
#Q1:WAP to check given number is positive.
print("Q1: check given number is positive.")
no = int (input("Enter your number: "))
if (no > 0):
    print("number is positive.")
print ("Done")


#Q2:WAP to check given number is positive or negative.
print ("\n\n\nQ2: check given number is positive or negative.")
no = int (input("Enter your number: "))
if (no >0):
    print ("Number is positive.")
else:
    print ("Number is negative.")
print("Done")



#Q1:WAP to check given number is zero, positive or negative.
print ("\n\n\nQ3:check given number is zero, positive or negative.")
no = int (input("Enter your number: "))
if (no == 0):
    print ("Number is zero.")
elif(no < 0):
    print ("Number is negative.")
else:
    print ("Number is positive.")
print("Done")


#Q2:WAP to check given number is even or odd.
print ("\n\n\nQ4:check given number is even or odd.")

no = int (input("Enter your number: "))
if (no%2 == 0):
    print ("Number is even.")
else:
    print ("Number is odd.")
print ("Done")


#Q3:WAP to accpect 2 number from user and do subtraction and division peration
# (Note: must subtract or divid smallest number from largest number.)
print("\n\n\nQ5:accpect 2 number for do subtraction and division peration.")

no1 = int (input("Enter your fisrt value\t:"))
no2 = int (input("Enter your second value\t:"))
if (no1>no2):
    sub = no1 - no2
    div = no1 / no2
else:
    sub = no2 - no1
    div = no2 / no2
print ("Subtraction is",sub, "and division is", div)


#4:WAP to print largest between 2 numbers.
print("\n\n\nQ6:largest between 2 numbers.")
no1 = int (input("Enter your fisrt value\t:"))
no2 = int (input("Enter your second value\t:"))
if (no1 == 0 and no2 ==0):
    print ("No comparison all 0.")
elif (no1<no2):
    print ("Number 2 is larger than number 1.")
elif (no1 == no2):
    print("All equal.")
else:
    print ("Number 1 is larger than number 2.")



#5:WAP to print the largest number between 3 numbers.
print("\n\n\nQ7:largest number between 3 numbers.")
NO1 = int (input("Enter your fisrt value\t:"))
NO2 = int (input("Enter your second value\t:"))
NO3 = int (input("Enter your third value\t:"))
if (NO1 == 0 and NO2 == 0 and NO3 == 0):
    print("No comparison all 0.")
elif (NO1 == NO2 and NO2 == NO3):
    print("The numbers are all equal")
elif (NO1 == NO3 and NO1>NO2):
    print("Number 1 and number 3 are larger than number 2.")
elif (NO2 == NO3 and NO2>NO1):
    print("Number 2 and number 3 are larger than number 1.")
elif (NO1 == NO2 and NO1>NO3):
    print("Number 1 and number 2 are larger than number 3.")
elif (NO3 > NO2 and NO3 > NO1):
    print ("Number 3 is the largest.")
elif (NO1 > NO2 and NO1 > NO3):
    print ("Number 1 is the largest.")
elif (NO2 > NO1 and NO2 > NO3):
    print ("Number 2 is the largest.")
else:
    print ("All equal.")


#6:WAP to
name = str (input("Enter your name\t\t: "))
tp = str (input ("Enter your TP number\t: "))
print ("Enter 5 subjects mark\t: ")
m1 = float (input ())
if (m1 > 100 or m1 < 0):
    print ("Wrong input: it must be less than 100 or greater than 0.\nKindly enter marks again.")
    m1 = int (input ())

m2 = float (input ())
if (m2 > 100 or m2 < 0):
    print ("Wrong input: it must be less than 100 or greater than 0.\nKindly enter marks again.")
    m2 = int (input ())

m3 = float (input ())
if (m3 > 100 or m3 < 0):
    print ("Wrong input: it must be less than 100 or greater than 0.\nKindly enter marks again.")
    m3 = int (input ())

m4 = float (input ())
if (m4 > 100 or m4 < 0):
    print ("Wrong input: it must be less than 100 or greater than 0.\nKindly enter marks again.")
    m4 = int (input ())

m5 = float (input ())
if (m5 > 100 or m5 < 0):
    print ("Wrong input: it must be less than 100 or greater than 0.\nKindly enter marks again.")
    m5 = int (input ())


total = m1 + m2 + m3 + m4 + m5
AVE = total / 5

print ("\tWELCOME TO APU \n\tRESULT HERE \n", "\n\nName \t\t\t: ",name, "\nTP number\t\t: ", tp, "\nTotal of the student\t: ", total, "\nYour percentage \t:", AVE)

if (AVE <= 100 and AVE >= 80):
    print ("\nYour grade\t\t: A+")
elif (AVE < 80 and AVE >=75):
    print ("\nYour grade\t\t: A")
elif (AVE < 75 and AVE >=70):
    print ("\nYour grade\t\t: B+")
elif (AVE < 70 and AVE >=65):
    print ("\nYour grade\t\t: B")
elif (AVE < 65 and AVE >=60):
    print ("\nYour grade\t\t: C+")
elif (AVE < 60 and AVE >=55):
    print ("\nYour grade\t\t: C")
elif (AVE < 55 and AVE >=50):
    print ("\nYour grade\t\t: C-")
else:
    print ("\nYour grade\t\t:D")


#Q7:
NAME = str (input ("Enter your name\t\t\t: "))
PA = float (input ("Enter your purchase amount\t: RM"))
TAX = int (input ("Enter the taxe code\t\t: "))

if(TAX == 0):
    ST = 0
elif (TAX == 1):
    ST = round (PA * 0.03, 2)
elif (TAX == 2):
    ST = round (PA * 0.05, 2)
elif (TAX == 3):
    ST = round (PA * 0.07, 2)
else:
    print ("Wrong input. Kindly enter again.")
    TAX = int (input ("Enter the taxe code\t\t: "))

TOTAL = PA + ST
print ("\n\nName\t\t\t:",NAME,"\nPurchase amount\t\t: RM",PA, "\nSales tax\t\t: RM", ST, "\nTotal amount due\t: RM",TOTAL)



#Q8:
T = int (input("Enter your body temperature: "))
if (T <= 37.5 and T >= 36.5):
    print ("\nYou are healthy.")
else:
    print ("\nYou are sick.")
'''


#Q9:
NAME = str (input ("Enter your name\t\t\t: "))
PA = float (input ("Enter your purchase amount\t: RM"))
if (PA >= 0 and PA <= 100):
    FB = PA * 0.98
if (PA >= 101 and PA <= 200):
    FB = PA * 0.97
if (PA >= 201 and PA <= 300):
    FB = PA * 0.96
else:
    FB = PA * 0.9

print ("\nName\t\t\t\t:",NAME, "\nPurchase amount\t\t\t: RM",PA,"\nFinal amount\t\t\t: RM", FB)
