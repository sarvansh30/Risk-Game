import time
import random


class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.current_player = None
        self.continents = []

    def add_continent(self, continent):
        self.continents.append(continent)

    def start(self):
        # Roll the dice to decide who goes first
        print("Roll the dice to decide who goes first. Press 1 to roll the dice.")
        input()
        player1_roll = 10
        player2_roll = 10
        while player1_roll == player2_roll:
            if player1_roll == player2_roll:
                print("Roll again!!")
            print("Dice is rolling...")
            time.sleep(2)
            player1_roll = random.randint(1, 6)
            player2_roll = random.randint(1, 6)
            print(f"{self.players[0].name} rolled a {player1_roll}")
            print(f"{self.players[1].name} rolled a {player2_roll}")

        if player1_roll > player2_roll:
            self.current_player = self.players[0]
        elif player1_roll < player2_roll:
            self.current_player = self.players[1]

        print(f"{self.current_player.name} goes first!")

    def switch_player(self):
        self.current_player = self.players[0] if self.current_player == self.players[1] else self.players[1]

    def undo_move(self, move):
        # Extract the details from the move
        action = move['action']
        from_territory_name = move['from_territory']
        to_territory_name = move['to_territory']
        num_armies = move['num_armies']

        # Get the territory objects
        from_territory = None
        to_territory = None
        for continent in self.continents:
            for territory in continent.territories:
                if territory.name == from_territory_name:
                    from_territory = territory
                if territory.name == to_territory_name:
                    to_territory = territory

        if action == 'place':
            # The action was to place armies
            # Decrease the number of armies in the from_territory
            from_territory.armies -= num_armies
        elif action in ['move', 'attack']:
            # The action was to move or attack
            # Increase the number of armies in the from_territory
            from_territory.armies += num_armies
            # Decrease the number of armies in the to_territory
            to_territory.armies -= num_armies
            # If the to_territory has no armies left and the action was 'attack', change the owner back
            if to_territory.armies == 0 and action == 'attack':
                to_territory.owner = to_territory.previous_owner  # You'll need to store the previous owner somewhere

    def attack(self):
        # Display current player's owned territories with their army numbers
        print(f"{self.current_player.name}'s territories:")
        for i, territory in enumerate(self.current_player.territories):
            print(f"{i + 1}. {territory.name} (Armies: {territory.armies})")

        # Ask the player from which territory they want to attack
        from_choice = int(input("Choose a territory to attack from by number: ")) - 1
        from_territory = self.current_player.territories[from_choice]

        # Ask the player how many armies they want to use for the attack
        max_armies = from_territory.armies - 1  # Leave at least one army behind
        num_armies = int(input(f"Enter number of armies to use for the attack (1-{max_armies}): "))
        num_armies = min(max(num_armies, 1), max_armies)  # Ensure num_armies is between 1 and max_armies

        # Show all adjacent territories not owned by the player
        enemy_territories = [territory for territory in from_territory.adjacent_territories if
                             territory.owner != self.current_player]
        print("Adjacent territories owned by the enemy:")
        for i, territory in enumerate(enemy_territories):
            print(f"{i + 1}. {territory.name} (Armies: {territory.armies})")

        # Ask the player which territory they want to attack
        to_choice = int(input("Choose a territory to attack by number: ")) - 1
        to_territory = enemy_territories[to_choice]

        # Roll dice for the attack
        attack_dice = sorted([random.randint(1, 6) for _ in range(num_armies)], reverse=True)
        defense_dice = sorted([random.randint(1, 6) for _ in range(min(to_territory.armies, 2))], reverse=True)

        # Print the dice rolls
        print(f"{self.current_player.name} rolled {attack_dice} for the attack")
        print(f"{to_territory.owner.name} rolled {defense_dice} for the defense")

        # Compare dice and remove armies
        for attack_die, defense_die in zip(attack_dice, defense_dice):
            if attack_die > defense_die:
                to_territory.armies -= 2
                if to_territory.armies < 0:
                    to_territory.armies = 0
                if to_territory.armies == 0:
                    # Remove the territory from the territories list of the previous owner
                    to_territory.owner.territories.remove(to_territory)
                    # Change the owner of the territory and add it to the territories list of the new owner
                    to_territory.owner = self.current_player
                    self.current_player.territories.append(to_territory)
                    to_territory.armies = num_armies
            else:
                self.current_player.armies += num_armies
        # Decrease the number of armies in from_territory by num_armies
        from_territory.armies -= num_armies

        if to_territory.owner == self.current_player:
            print("The attack was successful!")
        else:
            print("The attack was not successful.")

            # Display current player's owned territories with their army numbers
        print(f"{self.current_player.name}'s territories after the attack:")
        for i, territory in enumerate(self.current_player.territories):
            print(f"{i + 1}. {territory.name} (Armies: {territory.armies})")


    def place_or_move_armies(self):
        # Print the number of troops left for the current player
        print(f"Number of troops left for {self.current_player.name}: {self.current_player.armies}")

        # Show territories owned by the player and number of armies there
        for i, territory in enumerate(self.current_player.territories):
            print(f"{i + 1}. {territory.name} (Armies: {territory.armies})")

        # Ask the player if they want to place troops
        place_troops = input("Do you want to place troops? (yes/no): ")
        if place_troops.lower() == "yes":
            # Ask the player which territory they want to place troops in
            territory_choice = int(input("Choose a territory by number: ")) - 1
            chosen_territory = self.current_player.territories[territory_choice]

            # Ask the player how many troops they want to place
            num_troops = int(input("Enter number of troops to place (1-2): "))
            num_troops = min(max(num_troops, 1), 2)  # Ensure num_troops is between 1 and 2

            # Update the number of armies for the player and the territory
            self.current_player.armies -= num_troops
            chosen_territory.armies += num_troops

        # Ask the player if they want to move armies between territories
        move_armies = input("Do you want to move armies between territories? (yes/no): ")
        if move_armies.lower() == "yes":
            # Ask the player which territory they want to move armies from
            from_choice = int(input("Choose a territory to move armies from by number: ")) - 1
            from_territory = self.current_player.territories[from_choice]

            # Get adjacent territories owned by the current player
            owned_adjacent_territories = [territory for territory in from_territory.adjacent_territories if
                                          territory.owner == self.current_player]

            # If there are no owned adjacent territories, print a message and return
            if not owned_adjacent_territories:
                print("No adjacent territories owned by you.")
                return

            # Show owned adjacent territories
            print("Adjacent territories owned by you:")
            for i, territory in enumerate(owned_adjacent_territories):
                print(f"{i + 1}. {territory.name} (Armies: {territory.armies})")

            # Ask the player which territory they want to move armies to
            to_choice = int(input("Choose a territory to move armies to by number: ")) - 1
            to_territory = owned_adjacent_territories[to_choice]

            # Ask the player how many armies they want to move
            max_armies = from_territory.armies - 1  # Leave at least one army behind
            num_armies = int(input(f"Enter number of armies to move (1-{max_armies}): "))
            num_armies = min(max(num_armies, 1), max_armies)  # Ensure num_armies is between 1 and max_armies

            # Update the number of armies for the territories
            from_territory.armies -= num_armies
            to_territory.armies += num_armies

    def get_possible_moves(self, player):
        possible_moves = []
        # Iterate over all territories owned by the player
        for territory in player.territories:
            # If the action is to place armies, the possible move is just the territory
            possible_moves.append({'action': 'place', 'from_territory': territory.name, 'to_territory': None,
                                   'num_armies': 1})  # Assume placing 1 army
            # For move or attack actions, iterate over all adjacent territories
            for adjacent_territory in territory.adjacent_territories:
                # If the action is to move armies, the adjacent territory must be owned by the player
                if adjacent_territory.owner == player:
                    for i in range(1, territory.armies):  # Assume moving i armies
                        possible_moves.append({'action': 'move', 'from_territory': territory.name,
                                               'to_territory': adjacent_territory.name, 'num_armies': i})
                # If the action is to attack, the adjacent territory must not be owned by the player
                elif adjacent_territory.owner != player and territory.armies > 2:
                    for i in range(1, territory.armies):  # Assume attacking with i armies
                        possible_moves.append({'action': 'attack', 'from_territory': territory.name,
                                               'to_territory': adjacent_territory.name, 'num_armies': i})
        return possible_moves

    def apply_move(self, move):
        # Extract the details from the move
        action = move['action']
        from_territory_name = move['from_territory']
        to_territory_name = move['to_territory']
        num_armies = move['num_armies']

        # Get the territory objects
        from_territory = None
        to_territory = None
        for continent in self.continents:
            for territory in continent.territories:
                if territory.name == from_territory_name:
                    from_territory = territory
                if territory.name == to_territory_name:
                    to_territory = territory

        if action == 'place':
            # The action is to place armies
            # Increase the number of armies in the from_territory
            from_territory.armies += num_armies
        elif action in ['move', 'attack']:
            # The action is to move or attack
            # Decrease the number of armies in the from_territory
            from_territory.armies -= num_armies
            # Increase the number of armies in the to_territory
            to_territory.armies += num_armies
            # If the to_territory has no armies left and the action was 'attack', change the owner
            if to_territory.armies == 0 and action == 'attack':
                to_territory.owner = from_territory.owner

    def is_over(self):
        # The game is over if one player owns all territories
        return len(self.players[0].territories) == 0 or len(self.players[1].territories) == 0
