class Territory:
    def __init__(self, name, continent):
        self.name = name
        self.continent = continent
        self.owner = None
        self.armies = 0
        self.adjacent_territories = []

    def add_adjacent_territory(self, territory):
        self.adjacent_territories.append(territory)

    def set_owner(self, player):
        self.owner = player
        self.armies = 1  # Set the initial number of armies to 1 when a territory is claimed

    def update_armies(self, num_armies):
        self.armies = num_armies