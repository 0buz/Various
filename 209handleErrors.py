def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "magenta")
    if type(text) is not str:
        raise TypeError("text must be instance of str")
    if color not in colors:
        raise ValueError("color is invalid color")
    print(f"Printed {text} in {color}")

colorize("hell", 'cyan')

# try:
#     foobar
# except:
#     print("Problem!")
# print("after the try")


d={"name":"Billy"}

def get(d,key):
    try:
        return d[key]
    except KeyError:
        return None

print(get(d,"city"))

# while True:
#     try:
#         num = int(input("Please enter a number: "))
#     except ValueError:
#         print("That is not a number.")
#     else:                               # else will run when except will not
#         print("I am in the else. You have entered a number")
#         break
#     finally:                            # finally will run regardless what happens above
#         print("Runs no matter what")
# print("Rest of code.")

def divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("\nDivision by 0 error.")
    except TypeError as err:
        print("a and b must be int or float type.")
        print(err)
    else:
        print(f"{a} divided by {b} is {result}.")

divide(1,0)
divide("a",20)
divide(60,20)



