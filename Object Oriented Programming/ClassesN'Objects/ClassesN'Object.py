# Classes and Objects

class Greet:
    a = 12  # attribute

    def hello():  # method 
        print("How are you buddy?")


print(Greet.a)  # accessing attributes

Greet.hello()  # accessing methods


class Class:
    age = 17
    def show(self):  #Argument given to access method by object
        print("How are you man!")


obj = Class()  # Object defined

# Can access attribute and methods by object
print(obj.age)
obj.show()

class Bags:
    def __init__(self,material,zips,pockets):  #Constructor
        self.material = material  #instance attributes
        self.zips = zips
        self.pockets = pockets

reebok = Bags("Leather",5,4)    
campus = Bags("Polyster",4,2)

print(reebok.material)
print(reebok.zips)
print(campus.pockets)

class Animal:
    a= 34
    def __init__(self,name):
        self.name = name  #instance attributes
    
    def hello(self):  #captures location of instance/object
        print(f"Hello how are you my name is {self.name}")
    
    @classmethod
    def details(cls):  #captures location of class
        print(f"Hey how are you my age is {cls.a}")
    
lion = Animal("Lion")
lion.hello()
lion.details()
