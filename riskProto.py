from Continents import Continent
from Territory import Territory
from Player import Player
from Game import Game
import os
# Create continents
north_america = Continent("North America", 3)
south_america = Continent("South America", 2)

# creating territories in NA
alaska = Territory("Alaska", north_america)
north_america.add_territory(alaska)

ontario = Territory("Ontario", north_america)
north_america.add_territory(ontario)


# creating territories in SA
venezuela = Territory("Venezuela", south_america)
south_america.add_territory(venezuela)

brazil = Territory("Brazil", south_america)
south_america.add_territory(brazil)


# adding adjacent terrritories

alaska.add_adjacent_territory(ontario)

ontario.add_adjacent_territory(alaska)
ontario.add_adjacent_territory(venezuela)

venezuela.add_adjacent_territory(brazil)
venezuela.add_adjacent_territory(ontario)

brazil.add_adjacent_territory(venezuela)

# for continent in [north_america, south_america]:
#     for territory in continent.territories:
#         print(f"Territory: {territory.name}")
#         print("Adjacent territories:")
#         for adjacent_territory in territory.adjacent_territories:
#             print(f"- {adjacent_territory.name}")
#         print()

# Creating players
player1 = Player("PLAYER")
player2 = Player("AI")

game = Game(player1,player2)
game.add_continent(north_america)
game.add_continent(south_america)


# Print the names of the continents
# for continent in game.continents:
#     print(continent.name)
#     for territory in continent.territories:
#         print(f"Territory: {territory.name}")
#         print("Adjacent territories:")
#         for adjacent_territory in territory.adjacent_territories:
#             print(f"- {adjacent_territory.name}")
#             print()

game.start()

# Main game loop
# Main game loop
while True:
    # Print the current player's name
    print(f"{game.current_player.name}'s turn")

    # Get all unowned territories
    unowned_territories = [territory for continent in game.continents for territory in continent.territories if territory.owner is None]

    # If there are no unowned territories, break the loop
    if not unowned_territories:
        break

    # Print the unowned territories
    print("Unowned territories:")
    for i, territory in enumerate(unowned_territories):
        print(f"{i+1}. {territory.name}")

    # Ask the player to choose a territory
    choice = int(input("Choose a territory by number: ")) - 1

    # Assign the chosen territory to the current player
    chosen_territory = unowned_territories[choice]
    game.current_player.add_territory(chosen_territory)
    chosen_territory.owner = game.current_player
    chosen_territory.armies += 1
    game.current_player.armies -= 1

    # Switch to the other player
    game.switch_player()


for player in [player1, player2]:
    print(f"{player.name} owns the following territories:")
    for territory in player.territories:
        print(f"- {territory.name}")
    print()

# print(north_america.territories[0].armies)

input("Press Enter to continue")
os.system('cls' if os.name == 'nt' else 'clear')
print("Risk Game Start\n")

while True:
    print(f"{game.current_player.name}'s turn")
    print("Your choice?\n1 End Turn\n2Attack\n3Place Troops")
    sign=int(input())

    if sign==1:
        game.switch_player()
    elif sign==2:
        game.attack()
    else:
        game.place_or_move_armies()


