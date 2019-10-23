def sum_all_nums1(num1, num2,num3, ):
    return num1+num2+num3

# *args version
# args is a tuple

def sum_all_nums_args(*args):
    total=0
    for num in args:
        total+=num
    return total

print(sum_all_nums_args(2,5,6,7,8,8,9,4))  #use with any number of arguments
print(sum_all_nums_args())

# **kwargs  >>> Key Word Args
# stored as dictionary
# def fav_colours(a="purple",b="red",c="green")    >>>non-kwargs
def fav_colours(**kwargs):
    print(kwargs)
    for person, colour in kwargs.items():
        print(f"{person}'s favorite colour is {colour}.")

fav_colours(a="purple",b="red",c="green")

#==========================================================================================
def combine_words(word, **kwargs):
    if "prefix" in kwargs:
        return kwargs["prefix"]+word
    elif "suffix" in kwargs:
        return word+kwargs["suffix"]
    return word

print("\nkwarg Exercise: ", combine_words("do"))
print("\nkwarg Exercise: ", combine_words("do", prefix="un"))
print("\nkwarg Exercise: ", combine_words("do",suffix="er"))
print("\nkwarg Exercise: ", combine_words("do",pasta="fusili"))
#==========================================================================================

#==========================================================================================
# using * as argument  >>>> unpacking
def sum_all_nums_args(*args):
    total=0
    for num in args:
        total+=num
    return total

mylist=[2,5,6,7,8,8,9,4]
print("\nUnpacking: ",sum_all_nums_args(*mylist))  #use each of the list (or tuple) components a.k.a. unpack, to pass as arguments
#==========================================================================================

#==========================================================================================
# using ** as argument  >>>> dictionary unpacking
def display_names(first,second):
    print(f"{first} says hello to {second}.")

names={"first":"Alex","second":"Vinnie"}
display_names(**names)  #use dictionary unpack, and pass as arguments
#==========================================================================================

