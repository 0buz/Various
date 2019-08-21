#e.g. list is a class
# help(list)

nums=[1,2,3]   #nums is an object of type list

class User:
    def __init__(self, first, last, age):
        self.first = first     #   analogy: ".first" is the variable and "first" is the value; the self.attributes don't have to get the same name, but this is a convention
        self.last = last
        self.age = age

    def full_name(self):
        return f"{self.first} {self.last}"     #  this will return the instances particular first+last

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def enjoys(self,thing):
        return f"{self.first} enjoys {thing}."    # not self.thing; thing will be just a parameter in the instance just like any function parameter

    def is_senior(self):
        return self.age>=65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}! "

user1 = User("Joe","Smith",42)    # a new User class instance, in user1 object
user2 = User("Mike","Doe", 19)  # another instance of User class

print(user1.first, user1.last )
print(user2.age)
print("\n",user2.full_name())
print(user2.initials())
print(user2.enjoys("bananas"))

print(f"\nIs {user1.full_name()} senior? ", user1.is_senior())
print(user1.birthday())


#==============================================================================
class Comment:
    def __init__(self, username, text, likes = 0):
        self.username = username
        self.text = text
        self.likes = likes

c = Comment("Adi", "Pentru ca fraerii sa-nceapa sa cunoasca veteranii", 3)
print("\n",c.username,": ",c.text)

another_c=Comment("Gigi", "Va explic")
print(another_c.username, another_c.text, another_c.likes)

#==============================================================================


class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        try:
            self.balance += amount
            return self.balance
        except TypeError as err:
            print("Amount must be numeric.")
            print(err)

    def withdraw(self,amount):
        try:
            self.balance -= amount
            return self.balance
        except TypeError as err:
            print("Amount must be numeric.")
            print(err)

acct=BankAccount("Emma")
print("\nThe account owner is "+ acct.owner +".")
print("New balance:",acct.deposit(40))
print("New balance:",acct.deposit(30))
print("New balance:",acct.deposit("4t0"))
print("\nNew balance:",acct.withdraw(25))
print("New balance:",acct.withdraw(5))






