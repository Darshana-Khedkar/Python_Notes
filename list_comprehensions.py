#unique way to creting list

# mylist = []

# for letter in 'mystring':
#     mylist.append(letter)

# print(mylist)

#another way

mylist = [letter for letter in 'mystring']

print(mylist)

mylist2 = [num ** 2 for num in range(0 ,11)]
print(mylist2)
mylist3 = [ x for x in range(0,20) if x%2 == 0]
print(mylist3) # print even numbers

