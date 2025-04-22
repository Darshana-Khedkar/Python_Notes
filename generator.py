def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result
#create_cubes(10)
mylist = []
for x in create_cubes(10):
     
    mylist.append(x)
print(mylist)