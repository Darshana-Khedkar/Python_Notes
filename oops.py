from turtle import back


mylist = [1,2,3,4]
myset = set()
class  Dog():
 # species is a class object attribute
    species = 'mammal'
    def __init__(self,breed,name,sports):
        self.breed = breed
        self.name = name
        self.sports = sports


    def bark(self,numbers): #this is a method
        print("woof !")
        print("myjbsdhj {}jf{}".format(self.name,numbers))

mydog = Dog(breed= 'Lab',name = 'jully', sports = 'home')

print('my dog have {} breed, and my dog name is {}. my dog is very preety i loved my dog. its having sports {}.'.format(mydog.breed,mydog.name,mydog.sports))
# m1 =mydog.bark()
# print(m1)

#m1 = mydog.bark(numbers = 54)
#another way to calling instance
mydog.bark(8)