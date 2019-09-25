# Add up all odd numbers between 10 and 20
# Store the result in x:
x = 0

# YOUR CODE GOES HERE:
for nbr in range(10,20):
    if nbr%2 != 0:
        x += nbr
print("Odd number sum is {}.".format(x))