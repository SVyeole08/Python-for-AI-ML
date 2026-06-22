# 🐍 Python Learning Guide - main.py

Comprehensive collection of Python learning examples and exercises covering fundamental programming concepts.

---

## 📋 Table of Contents

1. String Manipulation
2. Type Conversion
3. Input/Output & F-strings
4. Conditional Statements
5. Loops
6. Data Structures
7. Exception Handling
8. File Handling

---

## 🔤 String Manipulation

### String Slicing

- Access characters and substrings using index
- Format: `string[start:end:step]`
- Example: `a[6:9:1]` gets index 6 to 8

### String Reversal

- Reverse string with negative step: `string[::-1]`
- Use for palindrome checking
- Used for word reversal

---

## 🔄 Type Conversion

### Converting Between Types

- `int()` - Convert to integer
- `float()` - Floating-point conversion
- `str()` - Convert to string
- `tuple()` - Convert to tuple
- `type()` - Check data type

### Example Conversions

- String to integer: `a = int("23")`
- Integer to float: `b = float(a)`

---

## 📥 Input/Output & F-strings

### User Input

- Use `input()` function for user input
- Default return type is string
- Must convert for other types
- Example: `age = int(input("Enter age: "))`

### Output Methods

1. **F-strings** (Recommended): `f"My name is {name} and my age is {age}"`
2. **Multiple arguments**: `print("My name is", name, "and my age is", age)`

---

## 🎯 Conditional Statements

### If/Elif/Else Examples

Used to execute code based on conditions.

| Problem                | Description              |
| ---------------------- | ------------------------ |
| Compare Numbers        | Find greater number      |
| Gender Greeting        | Greeting based on gender |
| Even/Odd Check         | Determine even or odd    |
| Voter Eligibility      | Check if age >= 18       |
| Leap Year Detection    | Identify leap year       |
| Temperature Categories | Classify temperature     |

### Leap Year Logic

A year is a leap year if:

- Divisible by 400: Leap year
- Divisible by 100 (not 400): Not leap
- Divisible by 4 (not 100): Leap year
- Otherwise: Not leap year

---

## 🔁 Loops

### For Loops - 13 Exercises

1. **Print String n Times** - Print "Hello world" n times
2. **Numbers 1 to n** - Print 1 to n
3. **Numbers n down to 1** - Print n down to 1
4. **Multiplication Table** - Print n × 1 through n × 10
5. **Sum 1 to n** - Calculate sum 1 to n
6. **Factorial** - Calculate n!
7. **Odd/Even Sum** - Sum odd and even numbers
8. **All Divisors** - Find all divisors
9. **Perfect Number Check** - Sum equals number
10. **Prime Check** - Verify prime/composite
11. **String Reversal** - Reverse a string
12. **Palindrome Check (String)** - Verify palindrome
13. **Character Analysis** - Count char/digit/special

### While Loops - 3 Exercises

1. **Extract Digits** - Print digits in reverse
2. **Reverse Number** - Reconstruct reversed number
3. **Palindrome Check (Integer)** - Verify palindrome

### Loop Operations

**Range Function:**

```python
range(5, 51, 5)  # Generate numbers from 5 to 50 in steps of 5
```

**Key Operations for While Loops:**

- `n % 10` - Extract last digit
- `n // 10` - Remove last digit
- `rev = rev * 10 + digit` - Build reversed number

---

## 📊 Data Structures

### 1. Lists

**Characteristics:**

- Mutable (can be modified)
- Support heterogeneous data
- Ordered collection
- Accessible by index

**Common Methods:**

- `append(elem)` - Add element to end
- `insert(index, elem)` - Insert at specific position
- `pop(index)` - Remove element at index
- `sort()` - Sort list in ascending order
- `reverse()` - Reverse list
- `remove(elem)` - Remove first occurrence of element
- `index(elem)` - Get index of element

**5 List Examples:**

1. **Separate Positive/Negative** - Split list into positive and negative
2. **Calculate Average** - Find average of list elements
3. **Find Greatest** - Find maximum and its index
4. **Find Second Greatest** - Find second largest element
5. **Check if Sorted** - Verify if list is sorted

---

### 2. Tuples

**Characteristics:**

- Immutable (cannot be modified)
- Defined using `()` or automatically recognized
- Support unpacking for value access
- Ordered collection

**Tuple Methods:**

- `index(elem)` - Get index of element
- `count(elem)` - Count occurrences of element

**Key Features:**

```python
tuple = (23, "aslkd", 234)      # With parenthesis
tup = 23, "aslkd", 234           # Without parenthesis
name, age, email = tuple_data    # Unpacking
```

**Use Case:** Return multiple values from function and unpack them

---

### 3. Sets

**Characteristics:**

- Store only unique values
- Auto-remove duplicates
- No guaranteed order
- Immutable elements

**Set Operations:**

- Union `a | b` - All elements from both sets
- Intersection `a & b` - Common elements only
- Difference `a - b` - Elements in a but not in b
- Symmetric Difference `a ^ b` - Elements in either but not both

**Set Methods (18 total):**

- `add(elem)` - Add element
- `remove(elem)` - Remove specific element
- `discard(elem)` - Remove with no error
- `pop()` - Remove random element
- `clear()` - Remove all elements
- `copy()` - Create independent copy
- `union()` / `|` - Union operation
- `intersection()` / `&` - Intersection
- `difference()` / `-` - Difference
- `difference_update()` - Update difference
- `intersection_update()` / `&=` - Update intersection
- `symmetric_difference()` / `^` - Symmetric diff
- `symmetric_difference_update()` / `^=` - Update diff
- `issubset()` / `<=` - Check subset
- `issuperset()` / `>=` - Check superset
- `isdisjoint()` - Check common elements
- `update()` / `|=` - Update union

---

### 4. Dictionaries

**Characteristics:**

- Store key-value pairs
- Accessed by key, not index
- Mutable
- Keys must be unique
- Ordered (Python 3.7+)

**Basic Operations:**

```python
d = {32: 23, 30: 200, 40: 400}
d[50] = 500          # Add new key-value pair
d[32] = 100          # Update existing value
value = d.get(32)    # Safe access
```

**Dictionary Methods (11 total):**

- `clear()` - Remove all elements
- `copy()` - Create independent copy
- `fromkeys(keys, value)` - Create dict
- `get(key, default)` - Get value safely
- `items()` - Get key-value pairs
- `keys()` - Get all keys
- `values()` - Get all values
- `pop(key)` - Remove key-value pair
- `popitem()` - Remove last pair
- `setdefault(key, value)` - Get or set
- `update(other_dict)` - Merge dictionaries

**4 Dictionary Examples:**

1. **Merge Dictionaries** - Combine dictionaries
2. **Sum All Values** - Calculate total values
3. **Count Occurrences** - Frequency dictionary
4. **Merge with Addition** - Combine with addition

**Traversing Dictionaries:**

```python
d = {10: 100, 20: 200, 30: 300, 40: 400}
for key in d:
    print(f"key {key} : value {d[key]}")
```

---

## ⚠️ Exception Handling

### Try/Except/Else/Finally Structure

```python
try:
    # Code that might raise exception
    result = a / b
except Exception as err:
    # Handle exception
    print(f"An error occurred due to {err}")
else:
    # Runs if no exception occurred
    print("No errors occurred")
finally:
    # Always runs
    print("I will always run")
```

### Raising Exceptions

Use `raise` to throw custom errors from your code:

```python
age = int(input("Enter your age:-"))
if age < 18:
    raise TypeError("You are not eligible")
print("You are eligible")
```

### Error Types

**Unfixable Errors (Cannot catch):**

- `SyntaxError` - Wrong syntax
- `IndentationError` - Bad spacing
- `TabError` - Mixing tabs/spaces

**Runtime Errors (Can catch):**

- `ZeroDivisionError` - Division by zero
- `ValueError` - Invalid value
- `TypeError` - Wrong type
- `NameError` - Undefined variable
- `IndexError` - Index out of range
- `KeyError` - Key not found

---

## 📁 File Handling

### File Modes

| Mode  | Purpose | File Behavior    | Description     |
| ----- | ------- | ---------------- | --------------- |
| `'r'` | Read    | Must exist       | Read file       |
| `'w'` | Write   | Create/overwrite | Write file      |
| `'a'` | Append  | Create if needed | Add to file     |
| `'x'` | Create  | Create only      | Create new file |

### Reading and Writing (Using `with` statement)

**Write to File:**

```python
with open("python.txt", "w") as f:
    f.write("Can create file named in path and write inside it as well")
```

**Read from File:**

```python
with open("python.txt", "r") as f:
    print(f.read())  # Read entire file content
```

**Append to File:**

```python
with open("python.txt", "a") as f:
    f.write(" can append by the mode 'a'")
```

### Why Use `with` Statement

✅ **Automatically closes file** after use
✅ **Closes file on errors** if exception occurs
✅ **Best practice** for file operations
✅ **Prevents resource leaks**

---

## 📌 Summary

Comprehensive Python resource covering:

- ✅ **Basic Syntax** - Variables, types, operators
- ✅ **Control Flow** - Conditionals and loops
- ✅ **Data Structures** - Lists, Tuples, Sets
- ✅ **Error Handling** - Try/except/finally
- ✅ **File I/O** - Read, write, append
- ✅ **40+ Examples** - Practical exercises

### Perfect For

- 🎓 Learning Python fundamentals
- 💪 Practicing with exercises
- 📚 Quick reference guide
- 🚀 Foundation for advanced topics

---

## 🎯 Learning Path Recommendation

1. Start with **String Manipulation** and **Type Conversion**
2. Practice **Input/Output** with user interactions
3. Master **Conditional Statements**
4. Perfect **Loops** (13 for + 3 while exercises)
5. Learn **Data Structures**
6. Understand **Exception Handling**
7. Practice **File Handling**

Each section includes examples and exercises!
