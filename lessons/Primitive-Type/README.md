# Variable and Data Type

## Variable

Variable names must follow a set of rules in order to be considered valid.
These rules include:

- Variable names can only contain letters, numbers, and underscores. They cannot contain spaces or special characters like `@`, `$`, `#` etc.
- Variable names cannot begin with a number. They must begin with a letter or an underscore.
- Variable names are case-sensitive, meaning that `MyVariable` and `myvariable` are considered to be different variables.
- Python has some reserved words that cannot be used as variable names. These include keywords such as `False`, `None`, `True`, `and`, `as`, etc.

How to declare and initialize a varible
- `varName = varValue`
    - `varName` is our variable declaration
    - `= varValue` is our variable initialization

*Example*

```python

"""
- It is important to use variable names that describe its uses.
- Also it is important to take note that python is a dynamic-typed language.
"""

fName = 'Juan'
lName = 'Dela Cruz'
age = 23

print(fName)
print(lName)
print(age)

# to insert arguments inside a String we use formatted String
print(f"Hi my name is {fName} {lName} and I am {age} years old.")

```

