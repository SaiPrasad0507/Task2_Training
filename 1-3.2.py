# checks the traffic signal 
Signal = int(input("Enter signal value: "))
if Signal == 1:
    print("Red Light - Stop")
elif Signal == 2:
    print("Yellow Light - Prepare to Stop")
elif Signal == 3:
    print("Green Light - Go")
else:
    print("Invalid signal value")