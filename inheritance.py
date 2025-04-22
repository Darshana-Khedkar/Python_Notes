#ability to reused code
#based class and inherited class

class Animal():
    def __init__(self):
        print("animal created")
        
    def who_am_i(self):
        print("i am a animal")
    def eat(self):
        print("im eating")


myanimal = Animal()
myanimal.who_am_i()
myanimal.eat()
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
    def who_am_i(self):
        print("Im a Dogghghg")
mydog = Dog()
mydog.who_am_i()