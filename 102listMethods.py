sounds = ["super", "ext1", "cali", "fragil", "istic", "expi", "ali", "docious"]

# Define your code below:
result = ''

for snd in sounds:
    result += snd

print(result.upper())

sounds.append("app1")   #can only add one item
print(sounds)

sounds.extend(["ext1","ext2","ext3"])   #adds multiple items to the end of the list in one go; note "[]" must be used
print(sounds)

sounds.insert(2,"insert")  #inserts item at the indicated index
print(sounds)


copy_sounds=sounds[:]    #to create a copy; see slicing
print(copy_sounds is sounds)

copy_sounds.pop()  #removes last item by defaut
print(copy_sounds)

popped=copy_sounds.pop(1) #removes item at index 1; can be put in a variable in case we want to do something with the filtered item
print(copy_sounds)
print("Popped item is "+popped)

copy_sounds.remove("app1")   # removes an item by value - first instance only - unlike pop which removes by index;
print(copy_sounds)

copy_sounds.clear()   #removes all list items
print(copy_sounds)



print("Index of element is " + str(sounds.index("ext1")))   # find the index of ext1
print("Index of element is " + str(sounds.index("ext1", 3)))   # find the index of ext1, after index 3
print("Index of element is still {}".format(sounds.index("ext1", 3, 12)))   # find the index of ext1, after index 3

print("Number of times item exists: {}".format(sounds.count("ext1")))

sounds.reverse() #reverses the elements of the list **in-place**
print(sounds)

sounds.sort()   #sorts the elements of the list **in-place**
print("Sorted list: {}".format(sounds))

#JOIN  - is technically a string method, not list
words=["Python", "is", "very", "interesting"]
print(words)

print('--'.join(words) + ".")
print('<<  >>'.join(words) + ".")
