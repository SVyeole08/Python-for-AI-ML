# Classes and Objects

## What is a Class and an Object?

- A **class** is a blueprint — it defines attributes (data) and methods (behavior).
- An **object** (also called an **instance**) is a real thing created from that blueprint.

---

## 1. Basic Class — `Greet`

I created a simple class to understand how attributes and methods work at the class level.

```python
class Greet:
    a = 12  # class attribute

    def hello():
        print("How are you buddy?")
```

- `a = 12` is a **class attribute** — it belongs to the class itself, not to any single object.
- `hello()` is a **method** — a function defined inside a class.
- I accessed them directly through the class name:
  - `Greet.a` → prints `12`
  - `Greet.hello()` → prints `"How are you buddy?"`

You can use a class without creating an object when methods do not need instance-specific data.

---

## 2. Using `self` and Creating Objects — `Class`

Next, How to create objects and use `self` to connect a method to a specific instance.

```python
class Class:
    age = 17

    def show(self):
        print("How are you man!")

obj = Class()
print(obj.age)
obj.show()
```

**What I learned:**
- `obj = Class()` creates an **object** (instance) of the class.
- `self` is the first parameter of instance methods — it refers to the current object.
- I can access attributes and methods through the object:
  - `obj.age` → `17`
  - `obj.show()` → prints the greeting

`self` is required so Python knows *which* object's method is being called.

---

## 3. Constructor and Instance Attributes — `Bags`

**`__init__` constructor**, which runs automatically when a new object is created.

```python
class Bags:
    def __init__(self, material, zips, pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets

reebok = Bags("Leather", 5, 4)
campus = Bags("Polyster", 4, 2)
```

- `__init__` is the **constructor** — it sets up each object when it is created.
- `self.material`, `self.zips`, and `self.pockets` are **instance attributes** — each object has its own values.
- I created two different objects with different data:
  - `reebok` → Leather, 5 zips, 4 pockets
  - `campus` → Polyster, 4 zips, 2 pockets
- Each object stores its own data, even though they share the same class blueprint.

This is a core idea in OOP: one class, many objects, each with its own state.

---

## 4. Instance Methods, Class Attributes, and `@classmethod` — `Animal`

Combined several OOP concepts in one class.

```python
class Animal:
    a = 34

    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f"Hello how are you my name is {self.name}")

    @classmethod
    def details(cls):
        print(f"Hey how are you my age is {cls.a}")

lion = Animal("Lion")
lion.hello()
lion.details()
```


| Concept | Example | Purpose |
|--------|---------|---------|
| Class attribute | `a = 34` | Shared by all instances of `Animal` |
| Constructor | `__init__(self, name)` | Sets `self.name` when object is created |
| Instance method | `hello(self)` | Uses `self` to access data for *this* object |
| Class method | `@classmethod` + `details(cls)` | Uses `cls` to access class-level data |

- `lion.hello()` uses **`self`** → reads the instance attribute `self.name` (`"Lion"`).
- `lion.details()` uses **`cls`** → reads the class attribute `cls.a` (`34`).

The `@classmethod` decorator tells Python that `details` receives the **class** (`cls`), not an instance (`self`).

---

## Summary of Class and Object

1. **Class attributes** — data shared by the whole class (`Greet.a`, `Animal.a`).
2. **Instance attributes** — data unique to each object (`self.material`, `self.name`).
3. **Methods** — functions inside a class (`hello`, `show`).
4. **`self`** — refers to the current instance in instance methods.
5. **`__init__`** — constructor that initializes objects when they are created.
6. **`@classmethod`** — method that works with the class itself using `cls`.
7. **Creating and using objects** — `obj = ClassName(...)` then calling `obj.method()`.

These are the building blocks of OOP in Python. From here, I can explore topics like inheritance, encapsulation, static methods, and more advanced class design.
