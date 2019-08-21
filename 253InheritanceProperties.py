class Animal:
    cool = True

    def __init__(self,name,species):
        self.name=name
        self.species=species

    def __repr__(self):
        return f"{self.name} is a {self.species}."

    def make_sound(self, sound):
        print(f"this animal says {sound}")


class Cat(Animal):  # Cat class inherits from Animal
    def __init__(self,name,species,breed,toy):
        # self.name = name        #this is duplication, which we should avoid
        # self.species = species  #this is duplication, which we should avoid
        #Animal.__init__(self,name,species="Cat")
        super().__init__(name,species="Cat")      #super() is preferred and does the same thing as the Animal line above
        self.breed = breed
        self.toy = toy

    def play(self):
        print (f"{self.name} plays with {self.toy}.")


# Make a new cat instance
blue = Cat("Blue","Cat","Scottish Fold","Ball")

# Because of inheritance, a Cat has access to:
blue.make_sound("Meow")
#print("Cool property inherited from Animal: ",blue.cool)

# blue is both a Cat and Animal (and base object)
# print(isinstance(blue, Cat))
# print(isinstance(blue, Animal))
# print(isinstance(blue, object))

print(blue)
blue.play()


print("\n")
print("==================================================================================")
#=======================================================================================

from copy import copy     #this will be used for the multiply method below; without this, we are not creating x new copies of the instance, but x references to the same one (see triplets example)
class Human:

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age>=0:
            self._age = age    # _age to be used as private/within class
        else:
            self._age = 0

    def __repr__(self):
        return f"Human named {self.full_name}"

    def __len__(self):      #define our own len method; see call below
        return self.age

    def __add__(self, other):          #define our own add (+) method; see call below
        if isinstance(other, Human):       # if other is an instance of Human
            return Human(first="Newborn",last=self.last,age=0)
        raise TypeError("Not a Human.")

    def __mul__(self, other):          #define our own multiply (*) method; see call below
        if isinstance(other, int):  # if other is an instance of int
            return [copy(self) for i in range(other)]       #copy comes from import above
        raise TypeError("Not a Human.")

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if new_age>=0:
            self._age = new_age
        else:
            self._age = 0

    @property     # getter property
    def age(self):
        return self._age

    @age.setter   # setter property
    def age(self,value):
        if value>=0:
            self._age = value
        else:
            raise ValueError("Age can't be negative.")
            self._age = 0

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

jane = Human("Jane","Andrews",35)
kevin = Human("Kevin","Ford",38)

#print(jane.age)
print("Use get_age() since there is no self.age anymore: ",jane.get_age())
jane.set_age(40)
# print(jane.age)
print("New age: ",jane.get_age())
print("\nAge using getter @property:",jane.age)

jane.age=20   # use setter property
print("Updated age:",jane.age)   #use getter

print("Full name:", jane.full_name)
print("\nAge using len:",len(jane))

print("Add method:", jane + kevin)
print("Multiply method:", jane * 2)
#print("Multiply method:", 2*jane)     #order of operands matters!!

triplets = jane *3
triplets[1].first='Mary'
print("\nTriplets ",triplets)

 


