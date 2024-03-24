class Player:
    def __init__(self, name):
        self.name = name
        self.territories = []
        self.continents = []
        self.armies = 10

    def add_territory(self, territory):
        self.territories.append(territory)
        territory.owner = self

    def add_continent(self, continent):
        self.continents.append(continent)

    def add_armies(self, num):
        self.armies += num

    def del_armies(self):
        self.armies-=1