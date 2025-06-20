# class Animal:
#     def __init__(self,name):
#         self.name = name

#      def eat(self)
#          print(f"{self.name} is eating.")

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed

#     def bark(self):
#         print(f"{self.name}, the {self.brreed} is barking!")


# dog1 = Dog("buddy", "GermanShephard")
# dog1.eat()
# dog1.bark()

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started. Vroom!")

    def stop_engine(self):
        print("Car engine stopped.")


class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started. Zoom!")


carObj = Car()
carobj.start_engine()
carObj.stop_engine()
bikeObj = Bike()
bikeObj.start_engine()        


