#checks if a student is eligible for a scholarship 
marks = int(input("Enter marks: "))
age = int(input("Enter age: "))
if marks >= 85 and age >= 18:
    print("Eligible for Scholarship.")
else:
    print("Not Eligible for Scholarship.")