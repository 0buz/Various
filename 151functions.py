def even_list():
    even=[]
    for x in range(1,50):
        if x%2 == 0:
            even.append(x)
    return even

print(even_list())


#========================================================================================
def even_list_comprehension():
    return [x for x in range(1,50) if x%2==0]

print("\n Comprehension: ", even_list_comprehension())
#========================================================================================

#========================================================================================
def single_letter_count(w,l):
    """Function returns letter count, case insensitive"""
    return w.upper().count(l.upper())


print('\nLetter count: ', single_letter_count("Hello", "x"))
#========================================================================================

#========================================================================================
def multiple_letter_count(string):
    """"Function returns a dictionary with counts for each letter, case insensitive"""
    return{l.lower():string.lower().count(l.lower()) for l in string}

print("\nMultiple letter count: ", multiple_letter_count("Antananarivo"))
#========================================================================================

#========================================================================================
def list_manipulation(lst,cmd,lct,val=None):
    """"Function takes a list, command, location and value, returns output of used command"""
    if cmd == "remove" and lct=="end":
        return lst.pop()   #remove last value
    elif cmd == "remove" and lct=="beginning":
        return lst.pop(0)
    elif cmd == "add" and lct=="beginning":
        lst.insert(0,val)
        return lst
    elif cmd == "add" and lct=="end":
        lst.append(val)
        return lst

mylist=["alb","rosu","negru","verde","albastru","galben"]
print(list_manipulation(mylist,"remove","end","valoare"))
print(mylist)
#========================================================================================


def intersection(l1,l2):
    """Function returns a LIST of common elements of two other lists"""
    return list(set(l1) & set(l2))   #using sets to do intersection

print("\nIntersection: ",intersection([1,2,3,4,5,6],[7,4,8,3]))

