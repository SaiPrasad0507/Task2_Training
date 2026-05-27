# checks if a person is eligible for a loan 
amount = float(input("Enter the amount: "))
age = int(input("Enter your age: "))
if amount > 1000 and age >= 18:
    print("Eligible for loan.")
else:
    print("Not eligible for loan.")