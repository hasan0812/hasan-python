class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def walk(self):
        print(f"{self.name} is walking")

dog = Animal("Dog")
dog.eat()
dog.walk()        
