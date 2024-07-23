class Cat:
    def __init__(self, name):
        print("inside Cat INIT")
        self.name = name

    def meow(self):
        print(f"{self.name} meows!")

class Cougar(Cat):
    def purr(self):
        print(f"{self.name} purrs!")

class Lion(Cat):
    def __init__(self, name, pride_name):
        print("inside Lion INIT")
        super().__init__(name)
        self.pride_name = pride_name

    def roar(self):
        print(f"{self.name} roars!")

instance = Cougar("Bella")
instance.purr()

instance_2 = Lion("Henry", "Big Boy")
instance_2.roar()

class puppy:
    species = 'canine'
    num_dogs = 0

    def __init__(self, name):
        self.name = name
        self.tricks = []
        puppy.num_dogs += 1

    @classmethod
    def register_stray(cls):
        return cls('coming soon')

    def add_tricks(self, new_trick):
        if new_trick not in self.tricks:
            self.tricks.append(new_trick)

    def bark(self):
        print(f"{self.name} says WOOF!")

    def perform_trick(self, trick):
        if trick in self.tricks:
            print(f"{self.name} performs {trick}")
        else:
            print(f"{self.name} doesn't know this {trick}")

otter = puppy("Otter")
otter.add_tricks("sit")
print(f"""
Name of dog = {otter.name}
Tricks of dog = {otter.tricks}
""")
otter.bark()
otter.perform_trick("down")
otter.perform_trick('sit')