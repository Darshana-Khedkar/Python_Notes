# try - this is the block of code to be attempted(may lead to an error)

# except - block of code will execute in case there is an error in try Block 
# finally - a final block of code to be executed, regardless of an error.

try:
    #want to attemp this code
    #may have ann error
    result = 10 + 10

except:
    print("hey  it looks you arent adding correctly!")
else:
    print("add went well!")
    print(result)