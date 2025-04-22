#diffrent object and classes shared same name

class Dog():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + "say woof!"
class Cat():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + "say nwoee"
    
niko = Dog("niko")
felix = Cat("felix")

print(niko.speak())
print(felix.speak())

for pet in [niko,felix]:
    print(type(pet))
    print(type(pet.speak()))

class Animal():
    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError("subclass must implement this abstract method")
myanimal = Animal('fred')

class Dog(Animal):
    def speak(self):
        return self.name+ " syays meow!"

fido = Dog("fido")
isis = Cat("chbsfjb")
print(fido.speak())
