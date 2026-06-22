# Encapsulation is concept in which we can control what data can be accessed and how it can be accessed.
# We can use encapsulation to hide the data and methods from the outside world.


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
print(car.__brand) # This will give an error because __brand is a private variable


# Getter and Setter methods.
# Getter and setter methods are used to get and set the value of a private variable.


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
print(car.get_brand())


