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
answer2=[number if number%2==0 else number+10 for number in numbers]
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


import time
start1=time.perf_counter()
numbers1=[1,2,3,4]
numbers2=[3,4,5,6]
answer3=[nbr for nbr in numbers1 if nbr in numbers2]
stop1=time.perf_counter()

start2=time.perf_counter()
jids=[]
jids_diff= ['94E56599139FCE4939', '1B46A35B5CA2280BA4', '5016BCDD1B12EB1617', '12FEBCDB49AEA390D9', '2D56F49AB63C3BA5FC', '755089292234A2F4B3', '81A319086E4FBA4FF8', 'D56F18355E6D8F6DEF', 'BDB591A6FA315A5ADA', 'B39F3E81200D9111F2', '009FCC3EF32BF39ADC', '41147E9A2A3A99E6E3', '6296DF34E534DCC02D', '6ECACFE409300CC818', '3649E634655D793B8F', 'BFD005C3C0C0BEDB44', 'C5725FE1126A2CA119', '48D843C4A706E0EB87', '8D0CBD7142002EE278', '0FB92F8A587DB406DF', 'F52C436F1AFC8897E6', 'F0558737DF63BC674E', 'F1F2DF8D8EA294FD75', '1D28A6B2A68EA1B65F', '3DFA91771ABE1A275D']
jids_diff=[jid for jid in jids if jid not in set(jids_diff)]

print(answer3)
print(len(numbers2))

stop2=time.perf_counter()


print("1st: ", str((stop1 -start1)))
print("2nd: ", str((stop2 -start2)))