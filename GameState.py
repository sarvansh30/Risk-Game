from Player import Player


class AIPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def minimax(self, game, depth, is_maximizing, player2):
        # Base case: the game is over or the maximum depth has been reached
        if depth == 0 or game.is_over():
            return self.evaluate(game)

        if is_maximizing:
            max_eval = float('-inf')
            for move in game.get_possible_moves(self):
                # Apply the move
                game.apply_move(move)
                eval = self.minimax(game, depth - 1, False, player2)
                # Undo the move
                game.undo_move(move)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in game.get_possible_moves(player2):
                # Apply the move
                game.apply_move(move)
                eval = self.minimax(game, depth - 1, True, player2)
                # Undo the move
                game.undo_move(move)
                min_eval = min(min_eval, eval)
            return min_eval

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
        return best_move
    def update_num_armies(self, num_armies):
        # Update the number of armies the AI player has
        self.num_armies = num_armies
