# Variable and Data Type

*Table of Contents*

- [Variable](#variable)
- Data Type
    - [String](#string)

## Variable
---

Variable names must follow a set of rules in order to be considered valid.
These rules include:

- Variable names can only contain letters, numbers, and underscores. _They cannot contain spaces or special characters like_ `@`, `$`, `#` etc.
- Variable names cannot begin with a number. _They must begin with a letter or an underscore_.
- Variable names are case-sensitive, meaning that `MyVariable` and `myvariable` are considered to be different variables.
- Python has some reserved words that cannot be used as variable names. These include keywords such as `False`, `None`, `True`, `and`, `as`, etc.

How to declare and initialize a varible
- `varName = varValue`
    - `varName` is our variable declaration
    - `= varValue` is our variable initialization

*Example*

```python

"""
- It is important to use variable names that describe their uses.
- Also it is important to take note that python is a dynamic-typed language.
"""

first_name = 'Juan'
last_name = 'Dela Cruz'
age = 23

print(fName)
print(lName)
print(age)

# to insert arguments inside a String we use formatted String
# f-string is another term for string interpolation
print(f"Hi my name is {first_name} {last_name} and I am {age} years old.")

```
## Data Types
---

### String

Series of characters. Anything inside a quotes is considered a string in Python, you can use single or double quotes around your strings like this:

```python
"""
Even if I use double or single quote. The program still recognize it as a string.
"""
first_name = 'Juan'
last_name = "Dela Cruz"

```

### Number

Python treats numbers in several different ways, depending on how they're being used.

*integers*
- any number without a decimal point is called an int.

*floats*
- any number with a decimal point is called a float

```python

banana = 45 # int
apple = 45.6 # float

```