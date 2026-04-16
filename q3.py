class Dog:
    """a dog"""
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"a Dog names {self.name}"
    def speak(self):
        print(f"{self.name} says woof!")

lulu = Dog("Lulu")
lulu.speak()

class Cat:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"a cat names {self.name}"
    def speak(self):
        print(f"{self} says moo")

toro = Cat("Toro")
toro.speak()