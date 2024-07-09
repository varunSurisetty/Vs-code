# # Create a variable and assign it a float
var = 6.4

# # Use print() and type() to print the data type of the variable in the output
print(type(var))

# # Use str() on the variable from step 1 and concatenate it with the string " is a float." then use print() to display the result
print(str(var) + " is a float.")

# # print() the string "Hello, I'm [name], it's nice to meet you!" including quotes (you will need to use the \' or \" escape sequence depending on whether you enclose your strings in single quotes or double quotes.)
print("Hello, I\'m varun surisetty, it\'s nice to meet you!")


# Create a variable called mixed_case and assign it the string "A Song of Ice and Fire"
mixed_Case = "A Song of Ice and Fire"
# Use .isupper() to check if mixed_case is a string of all upper case letters.  print() the result.
print(mixed_Case.isupper()) # False
# Use .islower() to check if mixed_case is a string of all lower case letters.  print() the result.
print(mixed_Case.islower()) # False
# Change all of the letters in mixed_case to upper case letters using .upper() and print() the result.
print(mixed_Case.upper())
# Change all of the letters in mixed_case to lower case letters using .lower() and print() the result.
print(mixed_Case.lower())
# Use the .istitle() method to check if mixed_case is title case and print the result.
print(mixed_Case.istitle())
# Create a variable called title_case and assign it the result of .title() being called on mixed_case.
title_Case = mixed_Case.title()
print(title_Case)

# Call startswith() on mixed_case with the letter mixed_case starts with as its argument.  print() the result.
print(mixed_Case.startswith("A"))
# Call endswith() on mixed_case with the letter mixed_case ends with as its argument.  print() the result.
print(mixed_Case.endswith("e"))
# Create a variable called words and assign it the result of split() being used on mixed_case.
words = mixed_Case.split(" ")
# print the variable "words"
print(words)
# Use the .join() method to join together all of the items in the list assigned to words as a single string.  Use .isalpha() to check if the string is made up entirely of letters.  Finally, use print() to display the result.
changed_word = " ".join(words)
print(changed_word.isalpha())
print(changed_word)

print("".join(words).isalpha())  