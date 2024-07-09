import random

gallons = random.randint(10, 25)
miles = random.randint(200, 400)

print("as the fuel tank used " + str(gallons) + " galloons of gas and the car travelled " + str(miles) + " miles, we got "+ str(miles//gallons) + "Miles per gallon (MPG).")
