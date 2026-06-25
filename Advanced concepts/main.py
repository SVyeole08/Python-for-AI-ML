import math

# Decorators


# Decorators are functions that modify the behavior of other functions. They are often used to add functionality to existing code without modifying it directly.

print()
print("Decorator: ")


def decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")

    return wrapper


@decorator
def greet():
    print("Hello, World!")


greet()

# Args and kwargs
# *args and **kwargs are used to pass a variable number of arguments to a function. *args is used to pass a variable number of non-keyword arguments, while **kwargs is used to pass a variable number of keyword arguments.

# Example of *args and **kwargs

print()
print("Args and kwargs: ")


def summation(func):
    def wrapper(*args, **kwargs):
        print("Before function is called.")
        func(*args, **kwargs)
        print("After function is called.")

    return wrapper


@summation
def addition(a, b, c):
    print(a + b + c)


addition(10, 234, 64)

# Example of *args


def sum(*args):
    s = 0
    for i in args:
        s += i
    return s


print(sum(12, 23, 52, 423, 25, 2323, 23))

# Comprehensions - One Liners
# Comprehension stands for creating a new list, set, or dictionary by applying an expression to each item in an iterable. It is a concise way to create new data structures from existing ones.

print()
print("Comprehensions: ")

# List comprehension
numbers = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
    32,
    33,
    34,
    35,
    36,
    37,
    38,
    39,
    40,
    41,
    42,
    43,
    44,
    45,
    46,
    47,
    48,
    49,
    50,
    51,
    52,
    53,
    54,
    55,
    56,
    57,
    58,
    59,
    60,
    61,
    62,
    63,
    64,
    65,
    66,
    67,
    68,
    69,
    70,
    71,
    72,
    73,
    74,
    75,
    76,
    77,
    78,
    79,
    80,
    81,
    82,
    83,
    84,
    85,
    86,
    87,
    88,
    89,
    90,
    91,
    92,
    93,
    94,
    95,
    96,
    97,
    98,
    99,
    100,
]
squares = [i for i in numbers if (i * i) % math.sqrt(i) == 0]
print(squares)

# Dictionary comprehension
squares_dict = {i: i * i for i in numbers if (i * i) % math.sqrt(i) == 0}
print(squares_dict)

# Set comprehension
squares_set = {i * i for i in numbers if (i * i) % math.sqrt(i) == 0}
print(squares_set)


# Lambda Functions
# Lambda functions are anonymous functions that can have any number of arguments but only one expression. They are often used for short, simple functions that are not reused elsewhere in the code.

print()
print("Lambda functions: ")

# Example of a lambda function

square = lambda x: x**2
print(square(5))

add = lambda x, y: x + y
print(add(10, 20))

check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(10))
print(check(11))

# Map, Filter, and Zip
# Map, filter, and zip are built-in functions that allow you to apply a function to an iterable, filter elements from an iterable, and combine multiple iterables into a single iterable, respectively.

print()
print("Map: ")

# Example of map
# folk = map(func, iterable)

tempCel = [0, 10, 20, 34.5]
tempKel = list(map(lambda x: x + 273.5, tempCel))
tempFah = list(map(lambda x: (x * (9 / 5)) + 32, tempCel))
print(tempKel)
print(tempFah)

# Example of filter
# folk = filter(func, iterable)

print()
print("Filter: ")

marks = [34, 67, 89, 23, 45, 90, 12, 56, 78, 99]
passed = list(filter(lambda x: x >= 35, marks))
print(passed)

# Example of zip
# folk = zip(func, iterable)

print()
print("Zip: ")

name = ["Alice", "Bob", "Charlie", "David", "Eve"]
age = [25, 30, 35, 40, 45]
people = list(zip(name, age))
print(people)

# Modules and Packages
print()
print("Modules: ")
# Modules are files containing Python code that can be imported and used in other Python programs.
# Packages are collections of modules organized in directories.

# I have created a module named maths.py in the same directory as this file. It contains two functions: addition and substraction. I will import this module and use its functions.

import maths  # Way to import modules

print(
    maths.addition(20, 34)
)  # Function of module maths is called and after running the code, it will return 54
print(maths.substraction(34, 30))  # Return 4

print()
print("Packages: ")
# I have created a package named Models in the same directory as this file. It contains a module named hello.py. I will import this package and use its functions.

from Models import hello  # Way to import packages

hello.hello()  # Function of package hello is called and after running the code, it will return "Hello from hello.py"

# If there is another package in Models then we import it like this:
from Models.model import dummy 

dummy.dummy()  # Function of package dummy is called and after running the code, it will return "Hello from dummy.py"

# There are big modules and packages named NumPy, Pandas, MatplotLib, Seaborn, etc.