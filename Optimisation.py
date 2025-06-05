def add(x,y):
    return x+y

print(add(10,12))

mylist = ["Ali","Ben","Cat","Doge","Eggbert","Fred","Grod"]

for word in mylist:
    print(f"Welcome, {word}!")

class Animal:
    def __init__(self):
        self.sound = ""

    def make_sound(self):
        print(f"{type(self).__name__} goes {self.sound}")

class Dog(Animal):
    def __init__(self):
        self.sound = "woof"

class Cat(Animal):
    def __init__(self):
        self.sound = "meow"

class Cow(Animal):
    def __init__(self):
        self.sound = "moo"


animals = [Dog(), Cat(), Cow()]
for a in animals:
    a.make_sound()

words = ["hello", "world", "!"]
sentence = " ".join(words)
print(sentence.strip())

fruit_stock = ["apple", "banana", "cherry"]
for i, item in enumerate(fruit_stock):
    print(i+1, item)
