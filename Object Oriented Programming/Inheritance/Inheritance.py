# Inheritance


class Mammals:  # Parent class
    def __init__(self, name):
        self.name = name

    def details(self):
        print(f"Hello my name is {self.name}")


class Humans(Mammals):  # Child class
    pass


obj1 = Mammals("Lion")
obj2 = Humans("Harsh")  # Humans class can access all attributes methods of Mammal class

obj1.details()
obj2.details()

print()

# Single Inheritance


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
        super().__init__(
            material, zips, pocks
        )  # If you add new attributes or methods to child class then you have use super function to use attributes or methods of parent class; super function targets parent class
        self.color = color

    def details(self):
        print(f"Color is {self.color}")
        return super().details()


bag = BagFactory("Leather", 3, 5)
rebook_bag = rebook("Polyster", 4, 6, "Red")

rebook_bag.details()

print()

# Multilevel Inheritance


class BagFactory:  # parent of rebook
    def __init__(self, material, zips, pocks):
        self.material = material
        self.zips = zips
        self.pocks = pocks

    def details(self):
        print(f"Material is {self.material}")
        print(f"Zips are {self.zips}")
        print(f"Pockets are {self.pocks}")


class rebook(BagFactory):  # child of Bagfactory and parent of campus
    def __init__(self, material, zips, pocks, color):
        super().__init__(
            material, zips, pocks
        )  # If you add new attributes or methods to child class then you have use super function to use attributes or methods of parent class; super function targets parent class
        self.color = color

    def details(self):
        print(f"Color is {self.color}")
        return super().details()


class campus(rebook):  # child of rebook
    def __init__(self, material, zips, pocks, color, size):
        super().__init__(material, zips, pocks, color)
        self.size = size

    def details(self):
        print(f"Size of bag is {self.size}")
        return super().details()


bag = BagFactory("Leather", 3, 5)
rebook_bag = rebook("Polyster", 4, 6, "Red")
campus_bag = campus("Cotton", 2, 3, "Green", "12L")

bag.details()
rebook_bag.details()
campus_bag.details()

print()

# Multipla inheritance
"""In this inheritance multiple parent have single child; And the child can access all the attributes and methods of parents"""


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

print()
