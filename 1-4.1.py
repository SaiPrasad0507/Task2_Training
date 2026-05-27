#Login validation 
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful!")
elif username == "admin" and password != "1234":
    print("Incorrect password.")
elif username != "admin" and password == "1234":
    print("Incorrect username.")
else:
    print("Invalid username and password.")