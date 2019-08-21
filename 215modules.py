from random import choice,randint, shuffle
import math
import keyword

print(choice(["alb","negru","albastru","rosu","galben"]))
print("Square root: ",math.sqrt(15129))

def contains_keyword(*args):
    for arg in args:
        if keyword.iskeyword(arg):
            return True   #if at least one arg is a keyword, return True
    return False

print("\nContains keyword: ",contains_keyword("def","afdbkjhgkdhgu"))
 