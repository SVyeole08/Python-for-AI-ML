# Dunder Methods in Python

Dunder Methods (also known as Magic Methods) are special methods in Python that have double underscores at the beginning and end of their names. They are used to define how objects of a class behave in various contexts. These methods are called implicitly when certain operations are performed on objects.

For example, when you write `obj + other`, Python internally calls `obj.__add__(other)`.

---

## Table of Contents

1. [Object Initialization and Representation](#object-initialization-and-representation)
2. [Comparison Operators](#comparison-operators)
3. [Arithmetic Operators](#arithmetic-operators)
4. [Reflected Arithmetic Operators](#reflected-arithmetic-operators)
5. [Augmented Assignment Operators](#augmented-assignment-operators)
6. [Unary Operators](#unary-operators)
7. [Bitwise Operators](#bitwise-operators)
8. [Type Conversion](#type-conversion)
9. [Container and Sequence Methods](#container-and-sequence-methods)
10. [Callable Objects](#callable-objects)
11. [Context Manager Methods](#context-manager-methods)
12. [Attribute Access](#attribute-access)
13. [Descriptor Methods](#descriptor-methods)
14. [Copy Methods](#copy-methods)
15. [Other Methods](#other-methods)

---

## Object Initialization and Representation

### `__init__(self, ...)`

Initializes the object after it has been created. Called automatically when a new instance is created.

**Example:**

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 25)  # __init__ is called automatically
```

### `__new__(cls, ...)`

Creates a new instance of the class. Called before `__init__`. Rarely overridden unless subclassing immutable types.

**Example:**

```python
class MyClass:
    def __new__(cls):
        print("Creating instance")
        return super().__new__(cls)
```

### `__del__(self)`

Destructor method called when an object is about to be destroyed (garbage collected).

**Example:**

```python
class MyClass:
    def __del__(self):
        print("Object is being destroyed")
```

### `__str__(self)`

Returns a human-readable string representation of the object.

**Example:**

```python
class Person:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Person: {self.name}"

print(Person("Alice"))  # Output: Person: Alice
```

### `__repr__(self)`

Returns an official string representation of the object, ideally evaluable code.

**Example:**

```python

class Person:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"Person('{self.name}')"

obj = Person("Alice")
print(repr(obj))  # Output: Person('Alice')
```

### `__format__(self, format_spec)`

Controls how the object is formatted using the `format()` function or f-strings.

**Example:**

```python
class Price:
    def __init__(self, amount):
        self.amount = amount
    
    def __format__(self, spec):
        return f"${self.amount:.{spec}f}"

price = Price(19.99)
print(f"{price:2}")  # Output: $19.99
```

---

## Comparison Operators

### `__eq__(self, other)`

Defines behavior for equality comparison (`==`).

### `__ne__(self, other)`

Defines behavior for inequality comparison (`!=`).

### `__lt__(self, other)`

Defines behavior for less-than comparison (`<`).

### `__le__(self, other)`

Defines behavior for less-than-or-equal comparison (`<=`).

### `__gt__(self, other)`

Defines behavior for greater-than comparison (`>`).

### `__ge__(self, other)`

Defines behavior for greater-than-or-equal comparison (`>=`).

**Example:**

```python
class Number:
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __lt__(self, other):
        return self.value < other.value

num1 = Number(5)
num2 = Number(10)
print(num1 == num2)  # Output: False
print(num1 < num2)   # Output: True
```

---

## Arithmetic Operators

### `__add__(self, other)`

Defines behavior for addition (`+`).

### `__sub__(self, other)`

Defines behavior for subtraction (`-`).

### `__mul__(self, other)`

Defines behavior for multiplication (`*`).

### `__truediv__(self, other)`

Defines behavior for true division (`/`).

### `__floordiv__(self, other)`

Defines behavior for floor division (`//`).

### `__mod__(self, other)`

Defines behavior for modulo operation (`%`).

### `__pow__(self, other)`

Defines behavior for exponentiation (`**`).

### `__divmod__(self, other)`

Defines behavior for `divmod()` function, returning both quotient and remainder.

**Example:**

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2  # Uses __add__
v4 = v1 * 2   # Uses __mul__
```

---

## Reflected Arithmetic Operators

Reflected arithmetic operators are called when the left operand doesn't support the operation. For example, `5 + obj` calls `obj.__radd__(5)` if `int.__add__` fails.

### `__radd__(self, other)`

Reflected addition (right-hand side).

### `__rsub__(self, other)`

Reflected subtraction (right-hand side).

### `__rmul__(self, other)`

Reflected multiplication (right-hand side).

### `__rtruediv__(self, other)`

Reflected true division (right-hand side).

### `__rfloordiv__(self, other)`

Reflected floor division (right-hand side).

### `__rmod__(self, other)`

Reflected modulo (right-hand side).

### `__rpow__(self, other)`

Reflected exponentiation (right-hand side).

### `__rdivmod__(self, other)`

Reflected divmod (right-hand side).

**Example:**

```python
class Number:
    def __init__(self, value):
        self.value = value
    
    def __radd__(self, other):
        return Number(other + self.value)

num = Number(5)
result = 10 + num  # Calls num.__radd__(10)
print(result.value)  # Output: 15
```

---

## Augmented Assignment Operators

These operators handle in-place operations (+=, -=, etc.).

### `__iadd__(self, other)`

In-place addition (`+=`).

### `__isub__(self, other)`

In-place subtraction (`-=`).

### `__imul__(self, other)`

In-place multiplication (`*=`).

### `__itruediv__(self, other)`

In-place true division (`/=`).

### `__ifloordiv__(self, other)`

In-place floor division (`//=`).

### `__imod__(self, other)`

In-place modulo (`%=`).

### `__ipow__(self, other)`

In-place exponentiation (`**=`).

**Example:**

```python
class Counter:
    def __init__(self, count):
        self.count = count
    
    def __iadd__(self, other):
        self.count += other
        return self

counter = Counter(5)
counter += 3  # Uses __iadd__
print(counter.count)  # Output: 8
```

---

## Unary Operators

### `__neg__(self)`

Unary negation (`-obj`).

### `__pos__(self)`

Unary positive (`+obj`).

### `__abs__(self)`

Absolute value (`abs(obj)`).

### `__invert__(self)`

Bitwise NOT (`~obj`).

**Example:**

```python
class Number:
    def __init__(self, value):
        self.value = value
    
    def __neg__(self):
        return Number(-self.value)
    
    def __abs__(self):
        return Number(abs(self.value))

num = Number(5)
print((-num).value)     # Output: -5
print(abs(Number(-3)).value)  # Output: 3
```

---

## Bitwise Operators

### `__and__(self, other)`

Bitwise AND (`&`).

### `__or__(self, other)`

Bitwise OR (`|`).

### `__xor__(self, other)`

Bitwise XOR (`^`).

### `__lshift__(self, other)`

Left shift (`<<`).

### `__rshift__(self, other)`

Right shift (`>>`).

### Reflected versions

`__rand__`, `__ror__`, `__rxor__`, `__rlshift__`, `__rrshift__` for right-hand operations.

### In-place versions

`__iand__`, `__ior__`, `__ixor__`, `__ilshift__`, `__irshift__` for augmented assignments.

**Example:**

```python
class Bits:
    def __init__(self, value):
        self.value = value
    
    def __and__(self, other):
        return Bits(self.value & other.value)
    
    def __lshift__(self, other):
        return Bits(self.value << other)

b1 = Bits(5)
b2 = Bits(3)
print((b1 & b2).value)   # Output: 1
print((b1 << 2).value)   # Output: 20
```

---

## Type Conversion

### `__int__(self)`

Converts object to an integer using `int(obj)`.

### `__float__(self)`

Converts object to a float using `float(obj)`.

### `__complex__(self)`

Converts object to a complex number using `complex(obj)`.

### `__bool__(self)`

Converts object to a boolean using `bool(obj)`.

### `__bytes__(self)`

Converts object to bytes using `bytes(obj)`.

### `__hash__(self)`

Returns the hash value of the object using `hash(obj)`.

**Example:**

```python
class Money:
    def __init__(self, amount):
        self.amount = amount
    
    def __int__(self):
        return int(self.amount)
    
    def __float__(self):
        return float(self.amount)
    
    def __bool__(self):
        return self.amount > 0

money = Money(10.50)
print(int(money))      # Output: 10
print(float(money))    # Output: 10.5
print(bool(money))     # Output: True
```

---

## Container and Sequence Methods

### `__len__(self)`

Returns the length of the container using `len(obj)`.

### `__getitem__(self, key)`

Gets an item from the container using `obj[key]`.

### `__setitem__(self, key, value)`

Sets an item in the container using `obj[key] = value`.

### `__delitem__(self, key)`

Deletes an item from the container using `del obj[key]`.

### `__contains__(self, item)`

Checks if an item is in the container using `item in obj`.

### `__iter__(self)`

Returns an iterator object for the container.

### `__next__(self)`

Returns the next item in an iterator.

### `__reversed__(self)`

Returns a reversed iterator using `reversed(obj)`.

**Example:**

```python
class CustomList:
    def __init__(self, items):
        self.items = items
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, value):
        self.items[index] = value
    
    def __contains__(self, item):
        return item in self.items

custom_list = CustomList([1, 2, 3])
print(len(custom_list))       # Output: 3
print(custom_list[0])         # Output: 1
print(2 in custom_list)       # Output: True
```

---

## Callable Objects

### `__call__(self, ...)`

Makes an object callable like a function using `obj()`.

**Example:**

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor

multiply_by_3 = Multiplier(3)
print(multiply_by_3(5))  # Output: 15
```

---

## Context Manager Methods

### `__enter__(self)`

Called when entering a `with` block. Returns a resource.

### `__exit__(self, exc_type, exc_val, exc_tb)`

Called when exiting a `with` block. Handles cleanup.

**Example:**

```python
class FileManager:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with FileManager('example.txt') as f:
    content = f.read()
```

---

## Attribute Access

### `__getattr__(self, name)`

Called when an attribute is not found through normal means. Provides a fallback mechanism.

### `__setattr__(self, name, value)`

Called when setting an attribute using `obj.attr = value`.

### `__delattr__(self, name)`

Called when deleting an attribute using `del obj.attr`.

### `__getattribute__(self, name)`

Called for every attribute access. Intercepts all attribute lookups.

**Example:**

```python
class DynamicAttributes:
    def __getattr__(self, name):
        return f"Attribute {name} not found"
    
    def __setattr__(self, name, value):
        print(f"Setting {name} to {value}")
        super().__setattr__(name, value)

obj = DynamicAttributes()
print(obj.missing)  # Output: Attribute missing not found
obj.new_attr = "value"  # Output: Setting new_attr to value
```

---

## Descriptor Methods

### `__get__(self, obj, objtype=None)`

Called when a descriptor is accessed.

### `__set__(self, obj, value)`

Called when a descriptor is set.

### `__delete__(self, obj)`

Called when a descriptor is deleted.

### `__set_name__(self, owner, name)`

Called when the descriptor is assigned to a class attribute.

**Example:**

```python
class Descriptor:
    def __init__(self):
        self.value = None
    
    def __get__(self, obj, objtype=None):
        return self.value
    
    def __set__(self, obj, value):
        self.value = value

class MyClass:
    attr = Descriptor()

obj = MyClass()
obj.attr = 10  # Uses __set__
print(obj.attr)  # Uses __get__, Output: 10
```

---

## Copy Methods

### `__copy__(self)`

Creates a shallow copy of the object.

### `__deepcopy__(self, memo)`

Creates a deep copy of the object.

**Example:**

```python
import copy

class MyClass:
    def __init__(self, value):
        self.value = value
    
    def __copy__(self):
        return MyClass(self.value)
    
    def __deepcopy__(self, memo):
        return MyClass(copy.deepcopy(self.value, memo))

original = MyClass([1, 2, 3])
shallow = copy.copy(original)
deep = copy.deepcopy(original)
```

---

## Other Methods

### `__sizeof__(self)`

Returns the size of the object in bytes using `sys.getsizeof()`.

### `__reduce__(self)`

Used for pickling objects. Returns a tuple describing how to reconstruct the object.

### `__reduce_ex__(self, protocol)`

Extended version of `__reduce__()` with protocol version.

### `__doc__`

Documentation string of the object.

### `__class__`

The class of the object.

### `__dict__`

Dictionary containing the object's attributes.

**Example:**

```python
import sys

class MyClass:
    def __init__(self):
        self.data = "example"
    
    def __sizeof__(self):
        return sys.getsizeof(self.__dict__)

obj = MyClass()
print(sys.getsizeof(obj))  # Uses __sizeof__
print(obj.__dict__)         # Output: {'data': 'example'}
print(obj.__class__)        # Output: <class '__main__.MyClass'>
```

---

## Summary

Dunder methods are powerful tools that allow you to:

- **Customize object behavior** for built-in operations
- **Make objects behave like built-in types** (lists, dicts, etc.)
- **Improve code readability** and elegance
- **Implement operator overloading** for domain-specific classes
- **Create intuitive APIs** for your classes

By implementing the appropriate dunder methods, you can make your custom objects integrate seamlessly with Python's ecosystem!
