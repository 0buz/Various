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

