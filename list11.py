l = [1,2,3,4]

l.append(4)
print(l)

l.count(10) # 0
l.count(1) # 1
x = [1,2,3]
x.append([4,5]) # adding [1,2,3[4,5]]
print(x)
x = [1,2,3]
x.extend([4,5]) # adding [1,2,3,4,5]
print(x)

l.index(2) ##1 return the index of item

# if yu want to add item accourding to index then use insert

l.insert(2,'insert') #2 is a index

print(l)


# pop() last element remove in list

ele = l.pop()

print(ele)

l.remove("insert")

print(l)

l.reverse()

print(l)

l.sort()
print(l)
