my_list = [1,2,3]

my_list1 = ['string',100,23.4,56,57,78]

print(len(my_list))
print(my_list1[0:5:2])
print(my_list1[:5])
print(my_list[1:])

print(my_list + my_list1)
new_list = my_list + my_list1
print(new_list[1])

#append element in list

my_list.append("addvalue2")
print(my_list)

#pop() remove element last element
my_list.pop()
print(my_list)
# stored pop item in popitems variable
popitem = my_list.pop()
print(my_list)
my_list.pop(0) #indexing

#sort() shorting the list ascending and descending order

fruit = ['a','b','r','d','c']
fruit.sort()
print(fruit)
#print(type(a)) # checking datatype

fruit.reverse()
print(fruit)