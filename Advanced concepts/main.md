# Advanced Python Concepts 🐍

## 1. Decorators

### What are Decorators?

Decorators are functions that modify or extend the behavior of another function without changing its original code.

### Syntax

```python
@decorator_name
def function():
    pass
```

### Example

```python
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
```

### Output

```bash
Before the function is called.
Hello, World!
After the function is called.
```

### Use Cases

* Logging
* Authentication
* Performance measurement
* Access control

---

# 2. *args and **kwargs

## *args

Allows a function to accept any number of positional arguments.

### Example

```python
def sum(*args):
    s = 0
    for i in args:
        s += i
    return s

print(sum(12, 23, 52, 423))
```

### Key Points

* Stored as a tuple.
* Useful when the number of inputs is unknown.

---

## **kwargs

Allows a function to accept any number of keyword arguments.

### Example

```python
def display(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

display(name="John", age=20)
```

### Key Points

* Stored as a dictionary.
* Useful for flexible configurations.

---

## Using *args and **kwargs in Decorators

```python
def summation(func):
    def wrapper(*args, **kwargs):
        print("Before function is called.")
        func(*args, **kwargs)
        print("After function is called.")
    return wrapper
```

This makes the decorator work with functions having any number of arguments.

---

# 3. Comprehensions

Comprehensions provide a concise way to create collections in a single line.

---

## List Comprehension

### Syntax

```python
[expression for item in iterable if condition]
```

### Example

```python
squares = [i for i in numbers if condition]
```

### Benefits

* Shorter code
* Better readability
* Faster than traditional loops

---

## Dictionary Comprehension

### Syntax

```python
{key:value for item in iterable if condition}
```

### Example

```python
squares_dict = {i: i*i for i in numbers}
```

### Output

```python
{
  1:1,
  2:4,
  3:9
}
```

---

## Set Comprehension

### Syntax

```python
{expression for item in iterable if condition}
```

### Example

```python
squares_set = {i*i for i in numbers}
```

### Key Feature

Automatically removes duplicate values.

---

# 4. Lambda Functions

## What is a Lambda Function?

A lambda function is a small anonymous function that can take multiple arguments but contains only one expression.

### Syntax

```python
lambda arguments : expression
```

---

## Example 1: Square

```python
square = lambda x: x**2
print(square(5))
```

### Output

```
25
```

---

## Example 2: Addition

```python
add = lambda x, y: x + y
print(add(10, 20))
```

### Output

```bash
30
```

---

## Example 3: Even/Odd Check

```python
check = lambda x: "Even" if x % 2 == 0 else "Odd"
```

### Output

```bash
Even
Odd
```

### When to Use

* Short functions
* map()
* filter()
* sorting operations

---

# 5. map()

## What is map()?

Applies a function to every element of an iterable.

### Syntax

```python
map(function, iterable)
```

---

## Example

```python
tempCel = [0, 10, 20, 34.5]

tempKel = list(map(lambda x: x + 273.5, tempCel))
tempFah = list(map(lambda x: (x * 9/5) + 32, tempCel))
```

### Output

```python
[273.5, 283.5, 293.5, 308.0]
[32.0, 50.0, 68.0, 94.1]
```

### Use Cases

* Data transformation
* Unit conversion
* Bulk calculations

---

# 6. filter()

## What is filter()?

Filters elements from an iterable based on a condition.

### Syntax

```python
filter(function, iterable)
```

---

## Example

```python
marks = [34, 67, 89, 23, 45, 90, 12, 56, 78, 99]

passed = list(filter(lambda x: x >= 35, marks))
```

### Output

```python
[67, 89, 45, 90, 56, 78, 99]
```

### Use Cases

* Selecting valid records
* Filtering data
* Removing unwanted values

---

# 7. zip()

## What is zip()?

Combines multiple iterables element-wise into a single iterable of tuples.

### Syntax

```python
zip(iterable1, iterable2, ...)
```

---

**Example**

```python
name = ["Alice", "Bob", "Charlie"]
age = [25, 30, 35]

people = list(zip(name, age))
```

### Output

```python
[
    ('Alice', 25),
    ('Bob', 30),
    ('Charlie', 35)
]
```

### Use Cases

* Combining related data
* Creating dictionaries
* Parallel iteration

---

## Quick Summary Table

| Concept                  | Purpose                               |
| ------------------------ | ------------------------------------- |
| Decorator                | Modify behavior of functions          |
| *args                    | Accept multiple positional arguments  |
| **kwargs                 | Accept multiple keyword arguments     |
| List Comprehension       | Create lists in one line              |
| Dictionary Comprehension | Create dictionaries in one line       |
| Set Comprehension        | Create sets in one line               |
| Lambda                   | Anonymous single-expression functions |
| map()                    | Apply a function to all elements      |
| filter()                 | Select elements matching a condition  |
| zip()                    | Combine multiple iterables            |

---

## Interview Tips

✅ Decorators are higher-order functions that return another function.

✅ `*args` → Tuple of positional arguments.

✅ `**kwargs` → Dictionary of keyword arguments.

✅ Lambda functions can contain only one expression.

✅ `map()` transforms data.

✅ `filter()` selects data.

✅ `zip()` combines data.

✅ Comprehensions are generally more readable and concise than loops.
