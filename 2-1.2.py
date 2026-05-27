#Parameters and arguments
def greet(name, greeting):
    return f"{greeting}, {name}!"
name = input("Enter your name: ")
greeting = input("Enter a greeting: ")
print(greet(name, greeting))
