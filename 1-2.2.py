#  ATM withdrawal process
balance = 3000
pin = 1234
user_pin = int(input("Enter your pin: "))
if user_pin == pin:
    print("Pin is correct.")
    amount = int(input("Enter the amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print("Withdrawal successful. Remaining balance:", balance)
    else:
        print("Insufficient balance.")