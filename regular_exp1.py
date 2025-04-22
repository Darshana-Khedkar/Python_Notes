import re
text = " the agents phone number is 404-7734-4388. call soon!"

print('phone' in text)

pattern = 'phone'

match = re.search(pattern,text)
match.start()
print(match)
