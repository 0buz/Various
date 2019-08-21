from functools import wraps    #this ensures that the function being passed in e.g. add keeps its metadata and not the wrapper metadata

def log_function_data(fn):
    @wraps(fn)          #this ensures that the function being passed in e.g. add keeps its metadata and not the wrapper metadata
    def wrapper(*args, **kwargs):
        """I AM WRAPPER FUNCTION"""
        print(f"you are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper


@log_function_data
def add(x,y):
    """Adds two numbers together."""
    return x + y

print(add.__doc__)
print(add.__name__)
help(add)




#==============================================================================================================
