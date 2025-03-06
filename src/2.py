import random
class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    def bark(self):
        return "Woof!"

d = Dog("Buddy", 3, "Golden Retriever")
print(d.bark())