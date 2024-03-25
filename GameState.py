from Player import Player
import time
import random

class AIPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def minimax(self, game, depth, is_maximizing, player2):
        if depth == 0 or game.is_over():
            return self.evaluate(game)

        if is_maximizing:
            best_score = float('-inf')
            for move in game.get_possible_moves(self):
                game.apply_move(move)
                score = self.minimax(game, depth - 1, False, player2)
                game.undo_move(move)
                if move['action'] == 'attack':
                    score += 30  # Add a large bonus for 'attack' moves
                elif move['action'] == 'move' and any(adjacent_territory.owner != self for adjacent_territory in
                                                      move['from_territory'].adjacent_territories):
                    score += 20  # Add a smaller bonus for 'move' actions that position the player to attack
                elif move['action'] == 'place' :
                    score += 10  # Add a small bonus for 'place' actions that reinforce the player's territories
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in game.get_possible_moves(player2):
                game.apply_move(move)
                score = self.minimax(game, depth - 1, True, player2)
                game.undo_move(move)
                best_score = min(score, best_score)
            return best_score

    def evaluate(self, game):
        score = 0
        # Increase score for each territory owned by the AI
        score += len(self.territories)
        # Increase score for each continent owned by the AI
        score += len(self.continents) * 5  # Assume owning a continent is 5 times as valuable as owning a territory
        # Increase score for each army owned by the AI
        score += self.armies
        return score

    def get_num_armies(game, move, action):
        # This is a simple example that always returns 1.
        # You should replace this with your own logic.
        return 1

    def choose_and_apply_move(self, game,player2):
        # Use the minimax function to choose the best move
        best_score = float('-inf')
        best_move = None
        possible_moves = game.get_possible_moves(self)
        for move in possible_moves:
            # Make the move
            game.apply_move(move)
            # Use the minimax function to get the score of the current game state
            score = self.minimax(game, 3, False,player2)  # Adjust the depth as needed
            # Undo the move
            game.undo_move(move)
            # Update the best score and best move
            if score > best_score:
                best_score = score
                best_move = move

        # After all moves have been evaluated, apply the best move
        game.apply_move(best_move)
        # If the action is 'attack', roll the dice and perform the attack
        if best_move['action'] == 'attack':
            for continent in game.continents:
                for territory in continent.territories:
                    if territory.name == best_move['from_territory']:
                        from_territory = territory
                    if territory.name == best_move['to_territory']:
                        to_territory = territory
            num_armies = best_move['num_armies']

            attack_dice = sorted([random.randint(1, 6) for _ in range(num_armies)], reverse=True)
            defense_dice = sorted([random.randint(1, 6) for _ in range(min(to_territory.armies, 2))], reverse=True)

            # Print the dice rolls
            print(f"{self.name} rolled {attack_dice} for the attack")
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
                        to_territory.owner = self
                        self.territories.append(to_territory)
                        to_territory.armies = num_armies
                else:
                    self.armies += num_armies
            # Decrease the number of armies in from_territory by num_armies
            from_territory.armies -= num_armies

            if to_territory.owner == self:
                print("The attack was successful!")
            else:
                print("The attack was not successful.")

            # Display current player's owned territories with their army numbers
            print(f"{self.name}'s territories after the attack:")
            for i, territory in enumerate(self.territories):
                print(f"{i + 1}. {territory.name} (Armies: {territory.armies})")

        return best_move
    def update_num_armies(self, num_armies):
        # Update the number of armies the AI player has
        self.num_armies = num_armies
