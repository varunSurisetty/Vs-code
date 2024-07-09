celsius = int(input("Enter celsius temp value in interger.\n"))

def farenheit(celsius):
#    if celsius >= 0 :
        return round((1.8*celsius + 32),1)
#    else
#        return null

print("The Fahrenheit equivalent of " + str(celsius) +" degrees Celsius is " + str(farenheit(celsius)))
print(farenheit(celsius))
