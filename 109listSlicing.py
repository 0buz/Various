#slicing creates a new list as opposed to in-place

# syntax   >>>>   list[start:end:step]

first_list=[11,12,13,14,15,16]

print(first_list[1:])   #returns all starting at index
print(first_list[-1:])  #returns that many elements from the end
print(first_list[:2])   #returns all ending at index
print(first_list[1:3])
print(first_list[1:-2])  #same as first_list[1:4]
print(first_list[::2])
print(first_list[2::-1])   #reverse order



#modifying portions of lists with slicing
first_list[1:3]=['a','b']    #replaces 12, 13 with a,b
print(first_list)

#On lists of strings we can chain slicing:
sounds = ["super", "ext1", "cali", "fragil", "istic", "expi", "ali", "docious"]

print(sounds[3][::-1])  #get item on index 3, reverse it




