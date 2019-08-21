from functools import wraps

#==============================================================================================================

def show_args(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        print(f"Tuple of args:",args)
        print(f"Dictionary of kwargs:", kwargs)
        return fn(*args,**kwargs)
    return wrapper

@show_args
def do_nothing(*args, **kwargs):
    pass

do_nothing(1,2,3,a="word",b="letter")
#==============================================================================================================

#==============================================================================================================
def double_return(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        """Returns the result two times, in a list"""
        val = fn(*args, **kwargs)
        return [val, val]
    return wrapper

@double_return
def add(x,y):
    return x+y

print(add(3,7))
#==============================================================================================================

#==============================================================================================================
def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        """Only execute if less than three arguments provided."""
        if len(args) >= 3:
            raise ValueError("Too many arguments.")
        return fn(*args,**kwargs)
    return wrapper

@ensure_fewer_than_three_args
def add_all(*nums):
    return sum(nums)

print("Sum is ",add_all(1,8))


#==============================================================================================================
def only_ints(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        """Only execute if arguments are integer."""
        # for arg in args:
        #     if type(arg) != int:
        #         raise TypeError("Please only invoke with integers.")

        #the above can be written using "any" + list comprehension
        if any([arg for arg in args if type(arg) != int]):
             raise TypeError("Please only invoke with integers.")
        return fn(*args,**kwargs)
    return wrapper

@only_ints
def add(x,y):
    return x+y

print(add(6,4))
#==============================================================================================================

#==============================================================================================================
def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        """Only execute if keyword argument exists as role = "admin"."""
        if kwargs.get('role')=='admin':
            return fn(*args,**kwargs)
        return "Unauthorised"
    return wrapper

@ensure_authorized
def access(**dct):
    return "Authorised"

print(access(role="admin"))
#==============================================================================================================

#==============================================================================================================

#passing argument to decorator; we need another layer; see "inner" below
def ensure_first_arg_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args,**kwargs):
           """Only execute if the first argument is."""
           if args and args[0] != val:   # if args exist and the first one is not equal to val
                raise ValueError(f"First arg needs to be {val}.")
           return fn(*args,**kwargs)
        return wrapper
    return inner

@ensure_first_arg_is(7)
def add_to_seven(a,b):
    return a+b

print("Sum is",add_to_seven(7,8))
#==============================================================================================================


#==============================================================================================================
from time import sleep

def delay(countdown):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args,**kwargs):
            """Execute after waiting x many seconds."""
            print(f"Waiting {countdown} seconds before running function.")
            sleep(countdown)
            return fn(*args,**kwargs)
        return wrapper
    return inner

@delay(3)
def say_hi():
    return "Hi"

print(say_hi())   
#==============================================================================================================