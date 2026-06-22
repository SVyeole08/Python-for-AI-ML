# Encapsulation

- Encapsulation is a concept in which we control what data can be accessed and how it can be accessed.
- It is used to hide data and methods from the outside world.
- In Python, encapsulation is achieved through access modifiers (public vs private) and getter/setter methods.

---

## 1. Public vs Private Attributes — `Factory`

- `Factory` defines public instance attributes in `__init__`: `type`, `tyre`, and `color`.
- `__brand` is a private class variable set to `"BMW"`.
- `details()` is a public method that prints the car's type, tyre, and color.

### Example

```python
class Factory:
    def __init__(self, type, tyre, color):  # Public variables
        self.type = type
        self.tyre = tyre
        self.color = color

    __brand = "BMW"  # This is a private variable

    def details(self):
        print(f"Type of car is {self.type}")
        print(f"Tyre of car is {self.tyre}")
        print(f"Color of car is {self.color}")

car = Factory("Sedan", "Michelin", "Red")
car.details()
print(car.__brand)  # This will give an error because __brand is a private variable
```

- `self.type`, `self.tyre`, and `self.color` are **public** — accessible from outside the class (e.g. `car.type`).
- `__brand` is **private** — a double underscore prefix triggers **name mangling** (stored internally as `_Factory__brand`).
- `car.__brand` raises an **AttributeError** — private variables cannot be accessed directly from outside the class.
- Public methods like `details()` allow controlled output without exposing private data.

---

## 2. Getter and Setter Methods — `Factory`

- Getter and setter methods are used to get and set the value of a private variable.
- `get_brand()` returns the value of `__brand`.
- `set_brand(brand)` updates the value of `__brand`.

### Example

```python
class Factory:
    def __init__(self, type, tyre, color):
        self.type = type
        self.tyre = tyre
        self.color = color

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

car = Factory("Sedan", "Michelin", "Red")
car.set_brand("BMW")
print(car.get_brand()) # Accessing private variable
```

### Output

```text
BMW
```

### Notes

- **Getter** — reads a private attribute through a method (`get_brand()`).
- **Setter** — writes to a private attribute through a method (`set_brand(brand)`).
- External code interacts with private data only through these methods, not by direct attribute access.
- Validation or extra logic can be added inside getter/setter methods when needed.

---

## Key Points

| Concept           | Example                                | Purpose                                            |
| ----------------- | -------------------------------------- | -------------------------------------------------- |
| Public attribute  | `self.type`, `self.tyre`, `self.color` | Accessible from outside the class                  |
| Private attribute | `__brand`                              | Hidden via name mangling                           |
| Public method     | `details()`                            | Exposes behavior without exposing raw private data |
| Getter            | `get_brand()`                          | Returns private data                               |
| Setter            | `set_brand(brand)`                     | Updates private data                               |

- **Encapsulation** — bundle data and methods and restrict direct access to internal details.
- **Public** — normal attributes and methods accessible from outside (`car.type`, `car.details()`).
- **Private (`__name`)** — name mangling prevents direct external access.
- **Getter / setter** — controlled read and write access to private attributes.
