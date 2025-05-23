


class character:
    def __init__(self, username, health, inventory):
        self.username = username
        self.health = health
        self.inventory = inventory


    def __str__(self):
        return f"{self.username}'s health is {self.health}"

    def add_health(self, amt):
        self.health += amt
    def add_inventory(self, item):
        self.inventory.append(item)