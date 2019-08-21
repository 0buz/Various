class User:

    active_users = 0   # this is a Class attribute, defined one time, for the class

    @classmethod   #this is a decorator identifying the following method as Class Method
    def display_active_users(cls):    #cls - means we will be working not with an instance (self), but with the class in this method
        return f"There are currently {cls.active_users} active users."

    @classmethod
    def from_string(cls,data_str):
        first,last,age = data_str.split(",")
        return cls(first,last,int(age))


    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users +=1   #User not self, because active_users is a class attribute, counting for all instances

    def __repr__(self):         #  allows defining a representation of an Instance; the representation can be whatever we want, for the string version of the instance
        return f"{self.first} is {self.age}."

    def logout(self):
        User.active_users -=1
        return f"{self.first} {self.last} has logged out."

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def enjoys(self,thing):
        return f"{self.first} enjoys {thing}."

    def is_senior(self):
        return self.age>=65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}! "




# print(User.active_users)    #called from the class
# user1 = User("Joe","Smith",42)    # a new User class instance, in user1 object
# user2 = User("Mike","Doe", 19)
# print("Number of active users:",User.active_users)
# print("\n",User.display_active_users())
#
# print(user2.logout())
# print("Number of active users:",User.active_users)
# print("\n",User.display_active_users())

tom =User.from_string("Tom,Jones,63")
print(tom.first)
print(tom.full_name())
print(tom.birthday())

j = User("Judy", "Flax", 32)
j = str(j)
print(j)    # whenever we call print (instance) after we turn the instance into a string, it will use the __repr_method
