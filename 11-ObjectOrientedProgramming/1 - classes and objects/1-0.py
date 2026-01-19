class Fruit:
    def __init__(self):
        self.name = "apple"
        self.colour = "red"

my_fruit = Fruit()

my_fruit.colour = "green"
my_fruit.name = "kiwi"

print(my_fruit.colour)
print(my_fruit.name)

# better approach:

class Fruit:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

apple = Fruit("apple", "red")
banana = Fruit("banana", "yellow")
kiwi = Fruit("kiwi", "green")

# methods:

class Fruit:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
    def details(self):
        print("my " + self.name + " is " + self.colour)

kiwi = Fruit("kiwi", "green")
kiwi.details()
        