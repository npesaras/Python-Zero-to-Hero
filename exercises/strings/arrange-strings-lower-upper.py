"""
Given string contains a combination of the lower and upper case letters.
Write a program to arrange the characters of a string so that all lowercase letters should come first.
"""

userInput = input("Please input word: ")

print('Original String:',userInput)

# Declare a variable that will contain our characters
lower = []
upper = []

for char in userInput:
    if char.islower():
        # it will add the lower character to lower list
        lower.append(char)
    else:
        # add uppercase characters to upper list
        upper.append(char)
        
# joining both list
lower_first = ''.join(lower + upper)
upper_first = ''.join(upper + lower)

# print the result

# lower first
print('Result lower first:',lower_first)

# upper first
print('Result upper first:',upper_first)