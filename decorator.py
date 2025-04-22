#def simple_func():
#want to do more stuff
#do simple  stuff return something

# 3 python has decorators that allows you to tack on extra functinality to an already existing function. 
# they use the @ operator and are then placed on top of the original function.


# @some_decorator
# def simple_func():
def new_decorator(original_func):
    def wrap_func():
        print("some extra code, before the original function")
    
        original_func()
        print('Some extra code aftetr the original functiokn')

    return wrap_func

def func_needs_decorator():
    print("i want  to be decorator!")
func_needs_decorator()

decorated_func = new_decorator(func_needs_decorator)


decorated_func()

@new_decorator
def func_needs_decorator():
    print("i want  to be decorator!")
