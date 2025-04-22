# def add_num(num1,num2):
#     return num1 + num2

# result = add_num(1,2)
# print("result is", result)

# def even_check(number):
#     result = number % 2 == 0
#     print(result)

#     return result
# even_check(20):



def check_even_list(num_list):
    #return all the even numbers in a list
    #placeholder variable
    even_numbers = []
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
            print(f"number is even {number}")
             
        else:
            pass
    print(even_numbers)

result = check_even_list([1,2,3,4,5,7,8,8,9,9,8])
