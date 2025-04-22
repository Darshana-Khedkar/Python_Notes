from collections import Counter
# mylist = [1,1,1,1,3,3,3,32,2,2,2,2,3]
# print(Counter(mylist))

#split()
# Counter print the value and keys in the foemat of dictinary
sentence = "how many times does each word sho up in this senrtence with a word"
print(Counter(sentence.lower().split()))
