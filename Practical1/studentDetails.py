# Student Details Program

name = input("Enter Student Name: ")
roll_no = int(input("Enter Roll Number: "))
course = input("Enter Course: ")

m1 = int(input("Enter Marks of Subject 1: "))
m2 = int(input("Enter Marks of Subject 2: "))
m3 = int(input("Enter Marks of Subject 3: "))

total = m1 + m2 + m3
percentage = total / 3

print("\n------ Student Details ------")
print("Name       :", name)
print("Roll No    :", roll_no)
print("Course     :", course)
print("Total Marks:", total)
print("Percentage :", percentage)

if percentage >= 90:
    print("Grade : A+")
    print("Result: Excellent")
elif percentage >= 75:
    print("Grade : A")
    print("Result: Very Good")
elif percentage >= 60:
    print("Grade : B")
    print("Result: Good")
elif percentage >= 40:
    print("Grade : C")
    print("Result: Pass")
else:
    print("Grade : F")
    print("Result: Fail")