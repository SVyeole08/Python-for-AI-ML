#Polymorphism

#OverLoading
class Demo:
    def show(self):
        print("First Method")

    def show(self, name):
        print("Hello", name)

obj = Demo()
obj.show("Sarvadnya")

#Overriding

class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


dog = Dog()
dog.sound()