nested_list=[[11,12,13],[14,15,16],[17,18,19]]

print(nested_list[0])
print(nested_list[1][2])
print(nested_list[2][-1])

#print comprehension method
print("\n")
[print(list) for list in nested_list]

print("\n")
[[print(val) for val in list] for list in nested_list]

#print a nested list with values [0,1,2], 3 times
print("\n")
ex5=[[i for i in range(3)] for j in range(3)]
print(ex5)

print("\n")
[[print(i) for i in range(10)] for j in range(10)]

