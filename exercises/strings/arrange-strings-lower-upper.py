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
sorted_list = ''.join(lower + upper)

# print the result
print('Result:',sorted_list)
