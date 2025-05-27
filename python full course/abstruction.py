'''
hiding the unnesscary information to the outside 
'''
#Simple code 
from abc import ABC , abstractmethod
class animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class dog(animal):
    def sound(self):
        return 'bark'
d=dog()
print(d.sound())




#other example 
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Bike(Vehicle):
    def start(self):
        print("Bike started")

class Car(Vehicle):
    def start(self):
        print("Car started")

b = Bike()
c = Car()
b.start()
c.start()
