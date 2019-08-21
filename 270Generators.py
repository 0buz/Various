#==================================================================================================
def week():
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
    for day in days:
        yield day

week1=week()
print(next(week1))
print(next(week1))
print(next(week1))
print(next(week1))
print(next(week1))
print(next(week1))
print(next(week1))
#print(next(week1))
#==================================================================================================


#==================================================================================================
def yes_or_no():
    answer="yes"
    while True:
        yield answer
        answer="no" if answer=="yes" else "yes"
#==================================================================================================


#==================================================================================================
import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1,15)

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))
#==================================================================================================

#==================================================================================================
def make_song(verses=99, beverage="soda"):
    for num in range(verses, -1, -1):
        if num > 1:
            yield "{} bottles of {} on the wall.".format(num, beverage)
        elif num == 1:
            yield "Only 1 bottle of {} left!".format(beverage)
        else:
            yield "No more {}!".format(beverage)
#==================================================================================================

#================= Generator Expressions ===================================================
import time

# SUMMING 10,000,000 Digits With Generator Expression
gen_start_time = time.time()  # save start time
print(sum(n for n in range(100000000)))
gen_time = time.time() - gen_start_time  # end time - start time

# SUMMING 10,000,000 Digits With List Comprehension
list_start_time = time.time()
print(sum([n for n in range(100000000)]))
list_time = time.time() - list_start_time

print(f"sum(n for n in range(10000000)) took: {gen_time}")
print(f"sum([n for n in range(10000000)]) took: {list_time}")
#==================================================================================================