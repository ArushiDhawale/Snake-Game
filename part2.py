# class inheritance

# you can create a class from a parent class with same, as well as additional attributes and functions.
# used to make a class more specific

class Animal:
    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("Breathing")


class Fish(Animal):
    def __init__(self):
        super().__init__()   # calls innit method from superclass (parent class)

    def swim(self):
        print("swimming")

    # if you want to add to a method
    def breathe(self):
        super().breathe()
        print("underwater")     # addition

nemo = Fish()
nemo.swim()
nemo.breathe()