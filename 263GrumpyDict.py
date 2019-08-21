class GrumpyDict(dict):    #custom class inheriting from the built-in dict
    #no need to define __init__() as we will use the one inherited from dict
    def __repr__(self):
        print(f"NONEYA!")
        return super().__repr__()   #call __repr__ from dict

    def __missing__(self, key):
        print(f"You want {key}? Ain't here.")

    def __setitem__(self, key, value):
        print("You want to change the dictionary? Fine...")
        super().__setitem__(key,value)    #call __setitem__ from dict

    def __contains__(self, item):
        print("Nope, ain't here!")
        return False    # just another example


d = GrumpyDict({"name":"Yoko","city":"New York"})
print(d)
d["new_key"]
d["new_key"] = "New Value"
print(d)
print("city" in d)


#==================================================================================================================

class Train:
    def __init__(self,num_cars):
        self.num_cars=num_cars

    def __repr__(self):
        return "{} car train".format(self.num_cars)

    def __len__(self):
        return self.num_cars

a_train=Train(8)
print("\n",a_train)
print(len(a_train))



