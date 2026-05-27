# checks if an employee is eligible for a bonus 
salary = float(input("Enter employee salary: "))
years = int(input("Enter years of service: "))

if salary >= 30000:
    if years >= 5:
        print("Employee is eligible for bonus.")
    else:
        print("Employee is not eligible because service is less than 5 years.")
else:
    print("Employee is not eligible because salary is below 30000.")