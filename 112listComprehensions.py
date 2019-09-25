with_vowels="a string with vowels."

print(''.join(char for char in with_vowels if char not in "aeiou"))

char_list=[char for char in with_vowels if char not in "aeiou"]
print(char_list)

print(''.join(char_list))

#List first letter of each name
names=["Ellie", "Tim", "Matt"]
answer=[name[0] for name in names]
print("\n", answer)

#names in reverse, all lowercase
answer=[name[::-1].lower() for name in names]
print("\n", answer)

#List even numbers
numbers=[1,2,3,4,5,6]
answer2=[number for number in numbers if number%2==0]
print(answer2)

# list intersection between the two lists
numbers1=[1,2,3,4]
numbers2=[3,4,5,6]
answer3=[nbr for nbr in numbers1 if nbr in numbers2]
print("\n", answer3)

#For all numbers between 1 and 100 (including), list all numbers divisible by 12.
integers=[nbr for nbr in range(1,101)]
divisible12=[div for div in integers if div%12==0]
print(divisible12)

#the above in one line
divisible12=[div for div in range(1,101) if div%12==0]
print("Divisiors optimised: ", divisible12)

#create list of consonants from string
ex4=[letter for letter in 'amazing' if letter not in 'aeiou']
print(ex4)




