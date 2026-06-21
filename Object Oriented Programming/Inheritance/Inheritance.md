# Inheritance

## What is Inheritance?

- **Inheritance** lets a **child class** reuse attributes and methods from a **parent class** (also called base/superclass).
- The child **is-a** kind of the parent — e.g. a `Humans` object is also a `Mammals` object.
- You avoid repeating code: define common behavior once in the parent, then extend or customize it in children.

---

## 1. Single Inheritance — `BagFactory` and `rebook`

One parent, one child. The child adds a new attribute and **overrides** a method, using `super()` to call the parent.

```python
class BagFactory:
    def __init__(self, material, zips, pocks):
        self.material = material
        self.zips = zips
        self.pocks = pocks

    def details(self):
        print(f"Material is {self.material}")
        print(f"Zips are {self.zips}")
        print(f"Pockets are {self.pocks}")

class rebook(BagFactory):
    def __init__(self, material, zips, pocks, color):
        super().__init__(material, zips, pocks)
        self.color = color

    def details(self):
        print(f"Color is {self.color}")
        return super().details()

bag = BagFactory("Leather", 3, 5)
rebook_bag = rebook("Polyster", 4, 6, "Red")

rebook_bag.details()
```

- **Single inheritance** = one parent (`BagFactory`) → one child (`rebook`).
- When the child adds new attributes (like `color`), override `__init__` and call **`super().__init__(...)`** so the parent still sets `material`, `zips`, and `pocks`.
- **`super()`** refers to the parent class — use it to reuse parent setup and methods.
- **Method overriding**: `rebook.details()` prints color first, then calls `super().details()` for material, zips, and pockets.
- `rebook_bag.details()` runs the child version, which chains to the parent version.

---

## 2. Multilevel Inheritance — `BagFactory` → `rebook` → `campus`

Inheritance in a chain: grandparent → parent → child. Each level can add attributes and override methods.

```python
class BagFactory:  # parent of rebook
    ...

class rebook(BagFactory):  # child of BagFactory, parent of campus
    ...

class campus(rebook):  # child of rebook
    def __init__(self, material, zips, pocks, color, size):
        super().__init__(material, zips, pocks, color)
        self.size = size

    def details(self):
        print(f"Size of bag is {self.size}")
        return super().details()

campus_bag = campus("Cotton", 2, 3, "Green", "12L")
campus_bag.details()
```

- **Multilevel inheritance**: `BagFactory` → `rebook` → `campus`.
- `campus` inherits from `rebook`, which inherits from `BagFactory` — so `campus` gets attributes and methods from **both** ancestors.
- `campus.__init__` calls `super().__init__(material, zips, pocks, color)`, which runs `rebook.__init__`, which calls `BagFactory.__init__`.
- `campus.details()` prints size, then `super().details()` → `rebook.details()` (color + parent details) → full bag info.
- One object (`campus_bag`) can hold data from all three levels: material, zips, pockets, color, and size.

---

## 3. Multiple Inheritance — `Humans`, `Animals`, and `Robot`

One child inherits from **two or more** parents. The child can use attributes and methods from each parent.

```python
class Animals:
    def __init__(self, strength):
        self.strength = strength

    def display(self):
        print(self.strength)

class Humans:
    def __init__(self, intelligence):
        self.intelligence = intelligence

    def display(self):
        print(self.intelligence)

class Robot(Humans, Animals):
    def __init__(self, intelligence, strength):
        Humans.__init__(self, intelligence)
        Animals.__init__(self, strength)

    def display(self):
        Humans.display(self)
        Animals.display(self)

robo = Robot(50, 50)
robo.display()
```

- **Multiple inheritance** = one child (`Robot`) with two parents (`Humans` and `Animals`).
- The child can access both `intelligence` and `strength`.
- With multiple parents, **`super()`** is trickier (MRO — Method Resolution Order), so here each parent is called explicitly: `Humans.__init__(self, ...)` and `Animals.__init__(self, ...)`.
- Both parents define `display()` — the child **overrides** it and calls each parent's `display()` separately.
- `robo.display()` prints both `50` (intelligence) and `50` (strength).

---

## Summary of Inheritance

| Type | Structure | Example in code |
|------|-----------|-----------------|
| Basic | Child inherits parent with no new code | `Humans(Mammals)` with `pass` |
| Single | One parent → one child | `rebook(BagFactory)` |
| Multilevel | Chain of classes | `BagFactory` → `rebook` → `campus` |
| Multiple | Several parents → one child | `Robot(Humans, Animals)` |

**Key concepts:**
1. **Parent / child** — child reuses and extends parent behavior.
2. **`super()`** — call the parent's `__init__` or methods from the child (common in single and multilevel inheritance).
3. **Method overriding** — redefine a method in the child (e.g. `details()`, `display()`).
4. **Extending attributes** — add new instance attributes in the child (`color`, `size`).
5. **Multiple inheritance** — combine traits from more than one base class; may need explicit `ParentClass.method(self)` calls.

Inheritance builds on classes and objects: define a base class once, then create specialized subclasses without duplicating code.
