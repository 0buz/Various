def fib_gen(max):
    x=0
    y=1
    count=0
    while count<max:
        x,y = y, x+y
        yield x
        count+=1


# for n in fib_gen(1000000):   #generators use significantly less memory than functions (not necesarily quicker)
#     print(n)



def get_multiples(nbr=1, count=10):
    next_nbr=nbr
    for i in range(count):
        yield next_nbr
        next_nbr = next_nbr + nbr

list_of_multiples=[x for x in get_multiples(3,7)]
print(list_of_multiples)

def get_unlimited_multiples(nbr=1):
    next_nbr=nbr
    while True:
        yield next_nbr
        next_nbr+=nbr

sevens=get_unlimited_multiples(7)       #get unlimited multiples of 7
print([next(sevens) for i in range(10)])   #print the first 10




