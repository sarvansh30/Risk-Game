class Continent:
    def __init__(self, name, bonus):
        self.name = name
        self.bonus = bonus
        self.territories = []

    def add_territory(self, territory):
        self.territories.append(territory)

    def is_controlled_by(self, player):
        return all(territory.owner == player for territory in self.territories)
