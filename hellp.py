class Dog:
    def __init__(self):
        self.name = "Dog"
        print("Dong was Born")

    def speak(self):
        print("YELP!", self.name)
    
    def wag(self):
        print("Dog's wag tail")

    def __del__(self):
        print("desroy!!")


class Puppy(Dog):
    pass