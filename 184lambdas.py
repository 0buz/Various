#lambdas are annonymous functions; lambdas have no name
# a common usecase is passing a function as argument within a function, when the arg function serves a one-off need; normally no need to store in variables

square = lambda num: num*num
print(square(6))

add = lambda a,b: a+b
print(add(3,11))
#===============================================================================================================================


#============================            MAP            ========================================================================
#another common usecase for lambdas is the "map" function
nums=[2,3,4,6,8,10]

doubles=map(lambda x: x*2, nums)    # this will double every item in nums i.e. the lambda will run for each item in nums
print("\n", list(doubles))   #doubles is initially an object that needs to be transformed into a list for example before printing

names=[
    {"first":"Alan", "second":"Wild"},
{"first":"Clint", "second":"Baker"},
{"first":"Mike", "second":"Lloyd"}
]

first_names=list(map(lambda x: x["first"], names))

print("\nMap-lambda on list of dictionaries",first_names)
#===============================================================================================================================

#===============================================================================================================================
def decrement_list(lst):
    return list(map(lambda x: x-1, lst))

print("\nDecrement list with lambda: ",decrement_list([5,8,11,17]))
#===============================================================================================================================


#============================            FLITER            =====================================================================
#similar to MAP, except it filters on the lambda formula, which will be True or False

names = ["adrian","alex", "jim", "andrew", "daniel"]
a_names = filter(lambda n: n[0] == 'a', names)    #filter names starting with a
print("\nNames starting with the given letter: ",list(a_names))
#===============================================================================================================================


#============================            FLITER + MAP           =================================================================
#example: Return a new list with the string "Your instructor is" + each value in the array, only if the value is less than 5 chars
names = ["adrian","alex", "jim", "andrew", "daniel"]
a_names = list(map(lambda name: f"Your instructor is {name}", filter(lambda value: len(value)<5, names)))
print("\nInstructors with short names list: ",a_names)
#===============================================================================================================================

def remove_negatives(lst):
    return list(filter(lambda x: x>=0, lst))

print("\nExclude negatives: ", remove_negatives([-2,5,6,-1,-8,8]))
