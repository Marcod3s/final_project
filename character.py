#class for user including stats and such




class character:
    def __init__(self, username, health, inventory, user_class):
        self.username = username
        self.health = health
        self.inventory = inventory
        self.user_class = user_class

    def __str__(self):
        return f"{self.username}'s health is {self.health} and my bag has {self.inventory} in it."

    def character_class_sel(self):
        user_name = input("")

#inventory goes into the character class

