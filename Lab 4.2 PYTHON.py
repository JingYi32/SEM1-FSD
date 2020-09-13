
#Q1.WAP to accpect 10 elements in program by using list. Display it.
mylist=[11,12,45,12,97,65,41,32,79,46]
print(mylist)



#WAP to accpect 10 values from user and store it in list. Display it.
mylist=[]
print("Enter 10 values here:")
for no in range (10):
    value = int (input("Enter your value:"))
    mylist.append(value)
print ("All values in the list: ",mylist)



#Q2.WAP to accept size of list elements. Add values in list as per defined size.
#Add all element of the list. Display list and addition of all list elements.
add = 0
mylist=[]
for no in range (int(input("Enter the size of the list element:"))):
    print("Enter",no + 1, "value:")
    value = int (input())
    add = add + value
    mylist.append(value)
print("All values of the list are: ",mylist,"\n",
      "Addition of all list elements is ",add,".")



#Q3.WAP to accept size of list from user and as per size enter elements in list.Print all EVEN elements of list.
add = 0
mylist=[]
for no in range (int(input("Enter the size of the list element:"))):
    print("Enter",no + 1, "value:")
    value = int (input())      
    mylist.append(value)
print("All values of the list are: ",mylist)
print ("The even numbers in the list are:")
for value in mylist:
    if (value%2 == 0):
        print (value)



#Q4.WAP to accept size of list from user and as per size enter elements in list. Print all EVEN elements and ODD elements of list. At the end display evensum and oddsum.
add = 0
mylist=[]
ES = 0
OS = 0
for no in range (int(input("Enter the size of the list element:"))):
    print("Enter",no + 1, "value:")
    value = int (input())      
    mylist.append(value)
print("All values of the list are: ",mylist)
print ("ODD List \tEVEN List")
for value in mylist:
    if (value%2 == 0):
        ES = ES + value
        print ("\t\t", value)
    else:
        OS = OS + value
        print (value)
print ("Sum of all odd number are:",OS,
       "\nSum of all even number are:", ES)



#Q5.WAP to read number of students in class and enter their names in list and display it at the end.
classlist=[]
size = int (input("Enter the total number of students in the class:"))
for name in range (size):
    name = str (input ("Enter the name of student:"))
    classlist.append(name)
print("The student in this class:",classlist)



#Q6.WAP to read number of total students in a class and enter their class_test marks in list. Display average of class_test.
mylist=[]
size = int (input("Enter the total number of students in the class:"))
add = 0
print ("Enter their class test marks:")
for no in range (size):
    print("Enter",no + 1, " student's mark:")
    value = int (input())      
    mylist.append(value)

for no in mylist:
    add = add + value
ave = add / size
print ("The Class Test Mark of The Students are: ", mylist)
print ("The average of class test is", round (ave,2), ("%"))



#Q7.WAP to create a list numbers using these number = 65, 75, 85, 95, 105 and check_number that prompt the user to enter a number to check that number is available or not in list.
#method1
mylist = [65,75,85,95,105]
no = int(input("Enter a value to check the number is available or not in list:"))
if no in mylist:
    print ("The number is available in the list.")
else:
    print ("The number is not available in the list.")
#method2
numbers=[65,75,85,95,100]
flag=0
check_number=int(input("Enter a value to check if it is in the list:"))
for x in range(len(numbers)):
    if check_number==numbers[x]:
        flag=1
        break
    else:
        flag=0
if flag==1:
    print("Number found in the list.")
else:
    print("Number not found in the list.")



#Q8.WAP to read name of student, TP Number and enter his/her all subject marks in list. Compute the total and percentage (Average) of a student. At the end display Name of student, TP Number, Total, Percentage and Grade of that semester. 
#(Note: 100-80 = A+          80-75 = A             75-70 = B+           70-65 = B             65-60 = C+            60-55 = C             55-50 = C-            50-0 = D/Fail).
name = input ("Enter student name\t:")
tp = int (input("Enter student TP number\t:"))
mark_list=[]
for mark in range (5):
    mark = int (input("Enter student mark:"))
    if (mark <=100 and mark >=0):
        mark_list.append(mark)
    else:
        print ("Kindly insert the mark again")
        mark = int (input("Enter student mark:"))
        
total = 0
for mark in mark_list:
    total = total + mark
ave = total / 5

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

print ("\n\n\tWelcone to APU Grade System\n\tHere is your result")
print ("Student Name\t\t\t:",name,"\nStudent TP number\t\t:",tp,"\nTotal mark of this semester\t:",total, "\nPercentage of this semester\t:",ave,"\nGrade\t\t\t\t:",grade)

