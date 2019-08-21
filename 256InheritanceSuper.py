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

class Moderator(User):

    active_mods=0

    def __init__(self,first,last,age,community):
        super().__init__(first,last,age)
        self.community=community
        Moderator.active_mods+=1

    @classmethod
    def display_active_mods(cls):
        return f"There are currently {cls.active_mods} active moderators."

    def remove_post(self):
        return f"{self.full_name()} removed a post from the {self.community}."

jim = Moderator("James","Brooks",25,"Music")
u1=User("Ben","Collins",46)
print(jim.full_name())
print(jim.community)

print("Total users:",User.display_active_users())   # active users includes Moderators (the inherited class)
print("Total Moderators:",Moderator.display_active_mods())
