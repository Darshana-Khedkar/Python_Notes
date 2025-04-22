# useful operators in python

# RANGE function

mylist = [1,2,3,4,5,6]

# for num in range(11):
#     print(num)  -- 1 to 10 numbers

# for num in range(0,11,2):
#     print(num) # start, ending -1, 2 is step to continue


# a = list(range(0,11,2))
# print(a)  # list range print

# index_count = 0

# for letter in "ababdjfufh":
     
#     print('At index {} the letter is {}'.format(index_count,letter))
#     index_count += 1

mylist1 = [1,2,3,4,5,6,7,8,9]
mylist2 = ['a0','b','c','r','f']

# a = list(zip(mylist1,mylist2))

# print(a)

# s = 'x ' in mylist2
# print(s) # False


#check in function in dictinari

d = {'mykey': 657}
print(657 in d.values()) # True u can also change insted of value add keys()

min(mylist)
max(mylist)

from random import shuffle
random_list = shuffle(mylist)

from random import randint

my = randint(0,10) #range start end

print(my)



