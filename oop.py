class car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def honk(self):
        print("BEEP BEEP!")

my_car = car('Porsche', 'Black')

print(f"Car name is: {my_car.brand}")
print(f"Car color is: {my_car.color}")
print(f"Car is in traffic: car does ")
my_car.honk()

def greet():
    print("Welcome")

prices = [55,68,77,36]

x = 5
city = "London"
is_open = True

print(type(greet))
print(type(prices))
print(type(x))
print(type(city))
print(type(is_open))

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Making a sound")

class Dog(Animal):
    def __init__(self,name, breed, age):
        # initialize attribute
        super().__init__(name)
        self.breed = breed
        self.age = age

    def sound(self):
        print("WOOF")

class Cat(Animal):
    def __init__(self, name, breed, age):
        super().__init__(name)
        self.breed = breed
        self.age = age

    def sound(self):
        print("MEOW")

my_dog = Dog("Jax", "Bulldog", 5)
my_cat = Cat("Lily", "Ragdoll", 2)

animals = [my_cat, my_dog]

for animal in animals:
    animal.sound()