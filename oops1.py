class Circle():
    pi = 3.14

    def __init__(self,radius = 1):
        self.radius = radius
        self.area = radius*radius*Circle.pi
    
    def get_circumference(self):
        print(self.radius * self.pi * 2)
        print(self.area )
    
my_circle = Circle(30)
print(my_circle.radius)
print(my_circle.pi)
my_circle.get_circumference()