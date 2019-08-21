class Character:
    def __init__(self,name,hp,level):
        self.name=name
        self.hp=hp
        self.level=level


class NPC(Character):
    def __init__(self,name,hp,level):
        super().__init__(name,hp,level)

    def speak(self):
        return f"{self.name} says: I am a NPC and I have {self.hp} health points, at level {self.level}."

dummy=NPC("Billy",86, 3)
print(dummy.speak())