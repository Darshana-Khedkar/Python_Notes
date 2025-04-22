#while loops 
#while some condition remains True
#syntax
# while some_boolean_condition:
#     #do something

# else:
#     #do something difrent

#in while loop x is changing after cheking
#so x going to be in infinity loop
# for example while my pool is not full keep filing my pool with water
# or while my dog are stil huungry, keep feeding my dogs
x = 0
while x < 5:
    print(f" {x} is less than 5")

    x = x + 1 # x += 1
    # thats why we use x +1

else:
    print(f"{x} is equal than 5")

# break, continue, pass
# break - break out of the current closet enclosing LookupError
# continue - goes to the top of the closet enclosing LookupError
# pass - does noting at all


# pass

# x = [1,2,3,4]

# for item in x:
#     pass
# print('endi of my script')
    

    # continue


# mystring = 'sammy'

# for letter in mystring:
#    if letter == 'a':
#       continue
#    print(letter)

# break

mystring = 'sammy'

for letter in mystring:
   if letter == 'a':
      break
   print(letter)


x = 0

while x < 5:
    if x == 2:
        continue
    print(x)
    x += 1

else:
    print("value is hhdbcjdb")

     
 


