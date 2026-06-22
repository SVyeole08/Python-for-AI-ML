# Decorators


# Decorators are functions that modify the behavior of other functions. They are often used to add functionality to existing code without modifying it directly.
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
