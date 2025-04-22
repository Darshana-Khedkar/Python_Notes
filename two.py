import one 
print("top level; in two.py")
one.func()

if __name__ == '__main__':
    print("two.py is beging run direcctly!")
else:
    print('one.py has been imorted1')