# Abstraction is the process of hiding the complex implementation details and showing only the functionality to the user.
# It is the process of showing only essential features and hiding the background details.
# In Python, abstraction is achieved through abstract classes and methods.
# Abstration does not exist in Python, but can be achieved through modules/libraries and classes.

from abc import ABC,abstractmethod #ABC is the abstract base class and abstractmethod is the abstract method.

class enforce(ABC):
    @abstractmethod
    def engineStart(self):
        pass

class bike(enforce):
    def engineStart(self):
        print("Engine of bike started")

class car(enforce):
    def engineStart(self):
        print("Engine of car started")

class truck(enforce):
    def engineStart(self):
        print("Engine of truck started")

obj1=bike()
obj2=car()
obj3=truck()

obj1.engineStart()
obj2.engineStart()
obj3.engineStart()