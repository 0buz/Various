# syntax: {_____:_____ for __ in ____}
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ^^^^^ REMEMBER SYNTAX   ^^^^^^^^^^^^^^^^^^^^






artist = {
    "first": "Billy",
    "last": "Young",
    "album": "Bling",
    "song": "Dalla"
}

upper_artist={
    k.upper():v.upper() for k,v in artist.items()
}

print(upper_artist)


num_list=[1,2,3,4,5]

print({num: "even" if num%2==0 else "odd" for num in num_list})
print({num: "even" if num%2==0 else "odd" for num in range(1,100)})

#upper case one key
upper_artist={
    k.upper() if k is 'album' else k:v.upper() for k,v in artist.items()
}

print("\n", upper_artist)


list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

dictio={list1[i]:list2[i] for i in range(len(list1))}
print("\n The two lists are now a dictionary: ", dictio)


person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = {k:v for k,v in person}
#OR
answer_dict = dict(person)  # when you have a list of pairs
print(answer)


vowels = {}.fromkeys(['a','e','i','o','u'], 0)
#OR
vowels = {}.fromkeys("aeiou",0)
print("\nvowels optimised: ", vowels)


#ASCII codes
alphabet = {k:chr(k) for k in range(65,91)}

print("\nAlphabet: ", alphabet)
