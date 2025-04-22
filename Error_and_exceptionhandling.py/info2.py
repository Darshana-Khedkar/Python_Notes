try:
    f = open('testfile','w')
    f.write("write a test line")
    a = int(input("enter a add "))
    result = 10 + a
except TypeError:
    print("there was a type error")

except OSError:
    print("hey your have an os error")
except:
    print('all other exceptions1')
finally:
    print("i always run")
