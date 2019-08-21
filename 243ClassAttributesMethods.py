class Pet:

    allowed=["cat","dog","fish","rat"]

    def __init__(self,name,species):
        if species not in Pet.allowed:
            raise ValueError(f"You cannot have a {species} pet.")
        self.name=name
        self.species=species

    def set_species(self,species):
        if species not in Pet.allowed:
            raise ValueError(f"You cannot have a {species} pet.")
        self.species = species




kitty=Pet("Gigi","cat")
doggy=Pet("Harry","dog")
#invalid_pet=Pet("Greg","dragon")
#print(invalid_pet.name)

kitty.set_species("rat")
print(kitty.species)
Pet.allowed.append("tiger")
kitty.set_species("tiger")
print(kitty.species)

print("\n",Pet.allowed, "ID:",id(Pet.allowed))
print(kitty.allowed, "ID:",id(kitty.allowed))      #while the instances also have allowed, which is just a reference to the class attribute "allowed" - see ID
print(doggy.allowed, "ID:",id(doggy.allowed))


#=================================================================================================================================

class Chicken:

    total_eggs=0

    def __init__(self,species,name,eggs=0):
        self.species=species
        self.name=name
        self.eggs=eggs

    def lay_eggs(self):
        self.eggs+=1
        Chicken.total_eggs+=1
        return self.eggs

c1=Chicken("Alice","Partridge Silkie")
c2=Chicken("Angela","Speckled Sussex")

print("\nTotal eggs: ",Chicken.total_eggs)
c1.lay_eggs()
print("c1 eggs:",c1.eggs)
print("\nTotal eggs: ",Chicken.total_eggs)
c2.lay_eggs()
c2.lay_eggs()
print("c2 eggs:",c2.eggs)
print("\nTotal eggs: ",Chicken.total_eggs)

