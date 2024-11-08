# Instance: A specific occurrence of a class
# Constructor: Creates an instance of a class

import questionary

class Cat:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

mimi = Cat("Mini", "Brown")