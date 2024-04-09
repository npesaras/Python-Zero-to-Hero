"""
Write a program to check if two strings are balanced
For example, string 1 and string 2 are balanced if all the characters in the string 1 are present in string 2. The character's position doesn't matter.
"""

string1 = input("Enter first string:")
string2 = input("Enter second string:")

# print inputted string
print(f'First String: {string1}\nSecond String: {string2}')

# create a function that compare two strings
def string_balance_test(string1,string2):
    flag = True
    for char in string1:
        if char in string2:
            continue
        else:
            flag = False
    return flag 

# Pass String 1 and String 2 to a function
compare_string = string_balance_test(string1,string2)

# Print the result
print("String 1 and String 2 are balanced?:",compare_string)