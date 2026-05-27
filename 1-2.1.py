# checks if a student is eligible for admission in college
n = int(input("Enter your marks: "))
age = int(input("Enter your age: "))
if n >= 75:
    if age >= 17:
     print("Eligible for Admission in College")
    else:
     print("Not Eligible for Admission in College")
    