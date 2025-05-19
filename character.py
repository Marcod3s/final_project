# class for user including stats and such


class character:
    def __init__(self, username, health,):
        self.username = username
        self.health = health
        #self.inventory = inventory
        # self.user_class = user_class
        # self.attacks = attacks

    def __str__(self):
        return f"{self.username}'s health is {self.health}"

