#Default values
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
name = input("Enter your name: ")
greeting = input("Enter a greeting (or press Enter for default): ")
if greeting:
    print(greet(name, greeting))
else:
    print(greet(name))