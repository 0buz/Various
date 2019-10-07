#tuples can be used as keys in dictionaries

locations = {
    (34.643, 45.123): "location 1",
    (1.323, 105.158): "location 2",
    (82.788, 40.746): "location 3",
    (12.477,120.699):"location 4"
}

print(type(locations))
print(locations)


x=(1,2,3,4,4,4)
print(x.count(4))
print(x.index(1))


#Sets do not have duplicates; there is no order in sets, so no "index"
s = {1,4,5,5}
print("Sets ignore duplicates: ",s)
s1 = set({20, 17, 1,2,3,4,5,6,7, 'a',8.74})
print("\ns1: ", s1)
print(6 in s1)

#add data to sets
s.add(2.6)
print("s.add: ", s)

#remove data from sets
s.remove(2.6)
print("s.remove: ", s)
#OR
s.discard(2.6)  #discard will not throw an error if the item does not exist in the set

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.intersection(b))
print("Short intersection: ",a & b)
print(b.intersection(a))

print(a.difference(b))
print("Short difference: ",a - b)

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

print(a.union(b))
print("Short union: ",a | b)

set_comprehension={x**2 for x in range(10)}
print("\n",set_comprehension)

string="mellons"

print("Vowel count in string is: ",len({char for char in string if char in "aeiou"}))


