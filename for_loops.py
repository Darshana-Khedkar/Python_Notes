#syntax of a for loop
# my_iterable = [1,2,3]
#for item_name in my_iterable:
#      print(item_name)

mylist = [1,2,3,4,5,6,7,8,9]

for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print(f'odd number: {num}')


        #

for  i in 'djjndsjndkn':
    print(i)



##
mylist2 = [(1,2,3),(5,6,7),(8,9,10)]

for a,b,c in mylist2:
    print(b)
#3
d = {'k1':1,'k2':4,'k4':6}
for ite in d:
    print(ite)

for key,value in d.items():
    print(value)
