# class car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     def honk(self):
#         print("BEEP BEEP!")

# my_car = car('Porsche', 'Black')

# print(f"Car name is: {my_car.brand}")
# print(f"Car color is: {my_car.color}")
# print(f"Car is in traffic: car does ")
# my_car.honk()

# def greet():
#     print("Welcome")

# prices = [55,68,77,36]

# x = 5
# city = "London"
# is_open = True

# print(type(greet))
# print(type(prices))
# print(type(x))
# print(type(city))
# print(type(is_open))

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def sound(self):
#         print("Making a sound")

# class Dog(Animal):
#     def __init__(self,name, breed, age):
#         # initialize attribute
#         super().__init__(name)
#         self.breed = breed
#         self.age = age

#     def sound(self):
#         print("WOOF")

# class Cat(Animal):
#     def __init__(self, name, breed, age):
#         super().__init__(name)
#         self.breed = breed
#         self.age = age

#     def sound(self):
#         print("MEOW")

# my_dog = Dog("Jax", "Bulldog", 5)
# my_cat = Cat("Lily", "Ragdoll", 2)

# animals = [my_cat, my_dog]

# for animal in animals:
#     animal.sound()

class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def start_engine(self):
        print(f"The {self.brand} engine is now running")

class Car(Vehicle):
    def __init__(self, brand, year):
        super().__init__(brand, year)
        self.wheels = 4

    def start_engine(self):
        print(f"The {self.brand} car engine purrs to life")

class Motorcycle(Vehicle):
    def __init__(self, brand, year):
        super().__init__(brand, year)
        self.wheels = 2

    def start_engine(self):
        print(f"The {self.brand} motorcycle engine roars to life")

my_car = Car("Porsche", 2025)
my_bike = Motorcycle("Kawasaki", 2025)

my_garage = [my_car, my_bike]

for transport in my_garage:
    transport.start_engine()
    print(f"This transport has {transport.wheels} wheels")
