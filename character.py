#class for user including stats and such
class character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.inventory = []
    def __str__(self):
        return f"{self.name}'s health is {self.health}"






#inventory goes into the character class

