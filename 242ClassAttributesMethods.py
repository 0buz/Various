class User:

    active_users = 0   # this is a Class attribute, defined one time, for the class

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users +=1   #User not self, because active_users is a class attribute, counting for all instances

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


print(User.active_users)    #called from the class
user1 = User("Joe","Smith",42)    # a new User class instance, in user1 object
user2 = User("Mike","Doe", 19)
print("Number of active users:",User.active_users)
print(user2.logout())
print("Number of active users:",User.active_users)
