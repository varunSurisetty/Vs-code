# Do all of this in a .py file in Pycharm

# Create a variable and assign it the string "Just do it!"

# Access the "!" from the variable by index and print() it

# Print the slice "do" from the variable

# Get and print the slice "it!" from the variable

# Print the slice "Just" from the variable

# Get the string slice "do it!" from the variable and concatenate it with the string "Don't ".  Print the resulting string, which should be "Don't do it!" where the "do it!" part is a slice.

String = "Just do it!"
print(String[-1])
print(String[5:7])
print(String[8:])
print(String[:5])
str1 = "Don\'t "
print(str1 + String[5:])