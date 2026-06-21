# Polymorphism

- Polymorphism is a core concept in Object-Oriented Programming (OOP).
- The word means **"many forms"**.
- In programming, it allows the same interface or method name to behave differently depending on the object or context.

---

# Types of Polymorphism

- Polymorphism can be achieved in Python in **two ways**:
  1. Method Overloading (limited support)
  2. Method Overriding

> In many compile-time languages, there are three types of polymorphism. However, Python does not support traditional method overloading directly.

---

## 1. Method Overloading

- Method overloading means having methods with the same name but different parameters.
- In Python, if multiple methods with the same name are defined inside a class, the **latest definition overwrites the previous one**.

### Example

```python
class Demo:
    def show(self):
        print("First Method")

    def show(self, name):
        print("Hello", name)

obj = Demo()
obj.show("Sarvadnya")
```

---

## 2. Method Overriding

- Method overriding occurs when a child class provides its own implementation of a method already defined in the parent class.
- Python decides at runtime which method to call based on the object's type.

### Example

```python
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


dog = Dog()
dog.sound()
```

### Output

```text
Dog barks
```

---

## Key Points

- Polymorphism allows one interface to have multiple implementations.
- Method Overloading is not directly supported in Python.
- Method Overriding is commonly used and supports runtime polymorphism.
- It improves code flexibility, reusability, and maintainability.