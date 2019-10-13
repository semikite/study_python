class Dog:
    def __init__(self, name):
        self.name = name
        print(self.name, " was Born")

    def speak(self):
        print("YELP!", self.name)
    
    def wag(self):
        print("Dog's wag tail")

    def m1(self):
        print("m1")
    
    def m2():
        print("m2")

    def __del__(self):
        print("desroy!!")

class Puppy(Dog):
    __hidden = "==========================="
    def __init__(self):
        self.name = "Puppy"
        self.color = "red"
        print("Puppy was Born")

    def __read_diary(self):
        print("Diary Content!!!")

    def wag(self):
        print("Puppy's wag tail")
        self.__read_diary()

    def speak(self):
        print("bow wow!", self.name)

    def change_color(self):
        self.color = "yellow"

    def static_method():
        print("xxxxxxxxxxxxxxxxxxxxxxx")

    def hidden(self):
        print(self.__hidden)

d = Dog("dog")
p = Puppy()

d.speak()
p.speak()


d.wag()
p.wag()

print(d.name,p.name)
print(p.color)

p.change_color()

print(p.color)

p.hidden()

Puppy.static_method()