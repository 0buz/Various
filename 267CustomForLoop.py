def my_for(iterable, func):
    iterator=iter(iterable)
    while True:
        try:
            thing = next(iterator)
        except StopIteration:
            print("End of iterator")
            break
        else:
            func(thing)

def square(x):
    print(x*x)
# my_for("hello")
# my_for([1,3,5,2,7,4,85])
my_for("word",print)
my_for([1,3,5,2,7,4,85], square)
