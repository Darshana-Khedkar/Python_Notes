s = set()
s.add(1)
s.add(2)
s.add(2)
s.add(4)
s.add(5)
print(s)
sc = {1,2}

 
print(s.difference(sc))

s1 = {2,3,4,5,5}
s2 = {3,4,5,6,6}

print(s1.difference_update())