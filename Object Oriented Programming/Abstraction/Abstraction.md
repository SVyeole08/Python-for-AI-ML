# Abstraction

- Abstraction is the process of hiding complex implementation details and showing only the functionality to the user.
- It focuses on **essential features** and hides background details.
- In Python, abstraction is achieved through **abstract classes** and **abstract methods** using the `abc` module.
- Python does not have a built-in `abstract` keyword — the `abc` module provides this behavior.

---

## 1. Abstract Base Class — `enforce`

- `ABC` (Abstract Base Class) and `@abstractmethod` are imported from the `abc` module.
- `enforce` is an abstract base class that defines a contract: any subclass must implement `engineStart()`.
- `engineStart()` is declared with `@abstractmethod` and has no implementation in the base class (`pass`).
- `enforce` cannot be instantiated directly — only its subclasses can be used.

### Example

```python
from abc import ABC, abstractmethod

class enforce(ABC):
    @abstractmethod
    def engineStart(self):
        pass
```

### Notes

- **`ABC`** — marks a class as abstract; it serves as a blueprint for other classes.
- **`@abstractmethod`** — marks a method that must be overridden in every child class.
- If a child class does not implement `engineStart()`, Python raises a **TypeError** when creating an object.

---

## 2. Implementing Abstraction — `bike`, `car`, `truck`

- `bike`, `car`, and `truck` inherit from `enforce`.
- Each class provides its own implementation of `engineStart()`.
- The user only calls `engineStart()` — the internal details of how each vehicle starts are hidden.

### Example

```python
class bike(enforce):
    def engineStart(self):
        print("Engine of bike started")

class car(enforce):
    def engineStart(self):
        print("Engine of car started")

class truck(enforce):
    def engineStart(self):
        print("Engine of truck started")

obj1 = bike()
obj2 = car()
obj3 = truck()

obj1.engineStart()
obj2.engineStart()
obj3.engineStart()
```

### Output

```text
Engine of bike started
Engine of car started
Engine of truck started
```

### Notes

- All three classes share the same method name (`engineStart`) but behave differently.
- Abstraction enforces a common interface while allowing each class to define its own logic.
- External code uses `obj.engineStart()` without needing to know how each engine actually starts.

---

## Key Points

| Concept | Example | Purpose |
|--------|---------|---------|
| Abstract base class | `class enforce(ABC)` | Defines a blueprint that cannot be instantiated directly |
| Abstract method | `@abstractmethod def engineStart(self)` | Must be implemented by all subclasses |
| Subclass | `bike`, `car`, `truck` | Provide concrete implementations |
| `abc` module | `from abc import ABC, abstractmethod` | Enables abstraction in Python |

- **Abstraction** — expose what an object does, hide how it does it.
- **Abstract class** — cannot create objects from it; used only as a base for other classes.
- **Abstract method** — declared in the base class, implemented in child classes.
- **Enforcement** — Python prevents creating a subclass object if abstract methods are missing.

Abstraction works with inheritance: the base class defines the required behavior, and each subclass fills in the details.
