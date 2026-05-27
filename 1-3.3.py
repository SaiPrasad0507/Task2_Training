# checks the weather and gives a message accordingly
weather = input("Enter the weather (sunny, rainy, snowy): ")
if weather == "sunny":
    print("It's a great day for outdoor activities!")
elif weather == "rainy":
    print("Don't forget to take an umbrella!")
elif weather == "snowy":
    print("Stay warm and drive safely!")
else:
    print("Invalid weather input.")