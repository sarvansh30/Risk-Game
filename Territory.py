class Territory:
    def __init__(self, name, continent):
        self.name = name
        self.continent = continent
        self.owner = None
        self.armies = 0
        self.adjacent_territories = []  # List to hold adjacent territories

    # def add_adjacent_territories(self, territories):
    #     for territory in territories:
    #         if territory not in self.adjacent_territories:
    #             self.adjacent_territories.append(territory)
    #             territory.adjacent_territories.append(self)  # Ensure the relationship is bidirectional

    def add_adjacent_territory(self, territory):
        self.adjacent_territories.append(territory)

    def set_owner(self,player):
        self.owner=player