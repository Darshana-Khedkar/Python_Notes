while True:
    try:
        result = int(input("please provide number:"))
    except:
        print("whoops that is not a number ")
        continue
    else:
        print("yes thank you")
        break
    finally:
        print("i will always run at the end!")
        
