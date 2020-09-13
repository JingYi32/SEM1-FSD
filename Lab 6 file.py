'''
#WAP to accept 3 students detail like stud_TP, Stud_Name, Stud_Add, Stud_Phone
#store in file and read data from file and display to user.

file=open("Q1.txt","w")
file.write("Student TP\t\tStudent Name\t\tStudent Address\t\tStudent Phone")
for i in range (3):
    Stud_Name = input("\nEnter your name\t\t\t: ")
    Stud_TP = input("Enter your student id\t\t: ")
    Stud_Add = input("Enter your address\t\t: ")
    Stud_Phone = int(input("Enter your contact number\t: "))
    file=open("Q1.txt","a")
    file.write("\n"+Stud_Name+"\t\t"+Stud_TP+"\t\t"+Stud_Add+"\t\t"+str(Stud_Phone))
    file.close()
file.close()
print("\n")
file = open("Q1.txt","r")
print (file.read())
file.close()


#Search data in the file.

data = input("Enter student name to be search in file:")
flag = 0
myfile = open("Q1.txt","r")
for line in myfile:
    if(line.startswith(data)):
        print (line)
        

myfile=open("Q1.txt","r")
data = input ("Enter Detail to Search in File:")
for line in myfile:
    line=line.rstrip()
    if not data in line:
        continue
    else:
        print(line)
'''
def opt_f():
    print("Your Options are:\n1.	Add new student detail.\n2.	View all student details.\n3.	Search Specific student detail.")
    opt = input('\nSelect your choice:')
    if (opt == "1"):
        display_f()
    elif (opt == "2"):
        file=open("Student.txt","r")
        print (file.read())
    elif (opt=="3"):
        file=open("Student.txt","r")
        data = input ("Enter Detail to Search in File:")
        for line in file:
            line=line.rstrip()
            if not data in line:
                print ("Data not found.")
                continue
            else:
                print(line)
    else:
        print ("Wrong insert, kindly select again.")
        opt_f()
        

def display_f():
    name = input ("\nEnter student name\t:")
    tp = int (input("Enter student TP number\t: TP"))
    sub = int (input("Enter total subjects in this semester:"))

    TOTAL = mark_f(sub)
    AVE = ave_f(TOTAL,sub)
    GRADE = grade_f(AVE)
    file=open("Student.txt","a")
    file.write(name+"\tTP"+str(tp)+"\t\t"+str(sub)+"\t"+str(mark_list)+"\t"+str(TOTAL)+"\t"+str(AVE)+"\t"+GRADE)
    file.close()

def mark_f(limit):
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
        opt_f()
        ans = input("Do you want to continue. '0' to continue, '-1' to Terminate:")
    print ("GOOD BYE")

mark_list=[]
option()
