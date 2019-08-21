import sys

list_comp=sys.getsizeof([x*10 for x in range(1000)])
gen_exp=sys.getsizeof(x*10 for x in range(1000))
print(f"List comprehension size: {list_comp} bytes.")
print(f"Generator expression size: {gen_exp} bytes.")



# sorted built in function
users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": [], "color": "purple"},
	{"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

print(sorted(users, key=len))   #sort on length of each dictionary in users list
print(sorted(users, key=lambda user: user['username']))
print(sorted(users, key=lambda user: len(user['tweets']), reverse=True))   #sort by number of tweets, in reverse


def extremes(lst):
    """Function to return min and max in the form of a tuple"""
    return (min(lst),max(lst))

print("\nMix and max are ",extremes([4,6,3,2,7,3,7]))


# reversed built in function; returns the reversed OBJECT
# use reversed if iterating over something in reverse
nums=[1,2,3,4,5]
print(list(reversed(nums)))

print("Won't work",reversed("hello"))

print("\nIterate in reverse:")
for x in reversed(range(0,10)):
    print(x)


def sum_even_values(*args):
    return sum(x for x in args if x%2==0)

print("\nSum of even values is: ", sum_even_values(6,3,3,4,5))

def sum_floats(*args):
    """Returns sum of items of type float, excludes other types"""
    return sum(x for x in args if type(x)==float)

print("\nSum of float items: ", sum_floats(1,1.1,2.2,"gigi",[2,8.9,22],3.3,"a"))


# zip built in function; returns an object consisting of pairs of tuples
# zips two or more lists/dictionaries etc

nums1=[1,2,3,4,5]
nums2=[6,7,8,9,10,12,13]
zipped = zip(nums1,nums2)
print("Zipped: ",list(zipped))

# unpacking with zip *; takes the first item from each tuple to create a tuple of firsts; same for the second etc
# common use case when working with complex data structures
five_pairs_two=[(0,1),(1,2),(2,3),(3,4),(4,5)]
print("Unpacked zip: ", list(zip(*five_pairs_two)))

# more zip examples
midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']


# returns dict with {student:highest score} USING DICT COMP
# {'dan': 98, 'ang': 91, 'kate': 78}

#final_grades = [max(grade) for grade in zip(midterms, finals)]
final_grades = {t[0]: max(t[1], t[2]) for t in zip(students, midterms, finals)}  #e.g. (t0, t1, t2) is (dan,80,98)

print(final_grades)

# same, but using map

#first example to get just the max grades
scores=map(
    lambda grade: max(grade),
    zip(midterms,finals)
)

print("\nMax grades using map: ", list(scores))

#now to get the max grade and student
grades = zip(
    students,
    map(
        lambda grade: max(grade),
        zip(midterms,finals)
    )
)

print("\nMax grades & students using map + dictionary: ", dict(grades))


#===================================================================================================
def interleave(s1, s2):
    """Function returns interweven/zipped string. .joins are required to convert back to string from tuple"""
    return ''.join(''.join(t) for t in zip(s1,s2))

print(interleave("set","now"))

#===================================================================================================

#===================================================================================================
def triple_and_filter(lst):
    """Function that filters out all items not divisible by 4. Returns new list consisting of remaining items multiplied by 3"""
    f_lst=filter(lambda x: x%4 !=0, lst)
    triple_lst=map(lambda x: x*3, f_lst)
    return list(triple_lst)

mylist=[3,4,8,5,32,2]
print("Simple version: ",triple_and_filter(mylist))

def triple_and_filter_optimised(lst):
    """Function that filters out all items not divisible by 4. Returns new list consisting of remaining items multiplied by 3"""
    return list(map(lambda x: x*3, filter(lambda x: x%4 !=0, lst)))

print("Optimised version: ",triple_and_filter_optimised(mylist))
#===================================================================================================

#===================================================================================================
def extract_full_name(dicts):
    """Returns list of strings of concatenated first + last"""
    firsts = list(map(lambda x: x["first"], dicts))   #get list of first names
    lasts = list(map(lambda x: x["last"], dicts))   #get list of last names
    full=list(zip(firsts,lasts))    #zip them
    return list(' '.join(name) for name in full)   #create list of full names

names = [
    {'first': 'Elie', 'last': 'Schoppik'},
    {'first': 'Colt', 'last': 'Steele'},
    {'first': 'Adrian', 'last': 'Peiu'}
]

print("\nFull names: ",extract_full_name(names))

def extract_full_name_one_line(dicts):
    """Returns list of strings of concatenated first + last"""
    #return list(' '.join(name) for name in zip(map(lambda x: x["first"], dicts),map(lambda x: x["last"], dicts)))   #create list of full names
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), dicts))

print("\nFull names - one line solution: ",extract_full_name_one_line(names))
#===================================================================================================

simple=sys.getsizeof(extract_full_name(names))
one_line=sys.getsizeof(extract_full_name_one_line(names))
print(f"Simple size: {simple} bytes.")
print(f"One line solution size: {one_line} bytes.")