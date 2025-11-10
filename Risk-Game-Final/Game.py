class Game:
    def __init__(self, player1, player2, territories, continents):
        self.player1 = player1
        self.player2 = player2
        self.territories = territories  # Dictionary of all territories
        self.continents = continents    # List of all continents
        self.current_player = player1
        self.move_history = []
        
    def get_possible_moves(self, player):
        """Get all possible moves for a player"""
        possible_moves = []
        
        # Get place moves (if player has unplaced armies)
        if hasattr(player, 'unplaced_armies') and player.unplaced_armies > 0:
            for territory in player.territories:
                possible_moves.append({
                    'action': 'place',
                    'territory': territory,
                    'num_armies': min(3, player.unplaced_armies)
                })
        
        # Get attack moves
        for territory in player.territories:
            if territory.armies > 1:  # Need at least 2 armies to attack
                for adjacent in territory.adjacent_territories:
                    if adjacent.owner != player and adjacent.owner is not None:
                        # Can attack with 1 to (armies-1) troops
                        max_attack = min(3, territory.armies - 1)
                        for num in range(1, max_attack + 1):
                            possible_moves.append({
                                'action': 'attack',
                                'from_territory': territory,
                                'to_territory': adjacent,
                                'num_armies': num
                            })
        
        # Get move/fortify moves
        for territory in player.territories:
            if territory.armies > 1:  # Need at least 2 armies to move
                for adjacent in territory.adjacent_territories:
                    if adjacent.owner == player:
                        # Can move 1 to (armies-1) troops
                        max_move = territory.armies - 1
                        for num in range(1, max_move + 1):
                            possible_moves.append({
                                'action': 'move',
                                'from_territory': territory,
                                'to_territory': adjacent,
                                'num_armies': num
                            })
        
        return possible_moves
    
    def apply_move(self, move):
        """Apply a move and save it to history"""
        if move is None:
            return
        
        action = move['action']
        
        if action == 'place':
            territory = move['territory']
            num_armies = move['num_armies']
            
            # Save state for undo
            old_armies = territory.armies
            self.move_history.append({
                'action': 'place',
                'territory': territory,
                'old_armies': old_armies,
                'num_armies': num_armies
            })
            
            territory.armies += num_armies
            
        elif action == 'attack':
            from_territory = move['from_territory']
            to_territory = move['to_territory']
            num_armies = move['num_armies']
            
            # Save state for undo
            old_from_armies = from_territory.armies
            old_to_armies = to_territory.armies
            old_owner = to_territory.owner
            
            self.move_history.append({
                'action': 'attack',
                'from_territory': from_territory,
                'to_territory': to_territory,
                'old_from_armies': old_from_armies,
                'old_to_armies': old_to_armies,
                'old_owner': old_owner,
                'num_armies': num_armies
            })
            
            # Simulate attack (simplified - just move armies for evaluation)
            from_territory.armies -= num_armies
            # Assume 50% success rate for evaluation
            if num_armies >= to_territory.armies:
                # Successful attack
                if old_owner:
                    old_owner.territories.remove(to_territory)
                to_territory.owner = from_territory.owner
                from_territory.owner.territories.append(to_territory)
                to_territory.armies = num_armies
            else:
                # Failed attack
                to_territory.armies -= (num_armies // 2)
                if to_territory.armies < 1:
                    to_territory.armies = 1
            
        elif action == 'move':
            from_territory = move['from_territory']
            to_territory = move['to_territory']
            num_armies = move['num_armies']
            
            # Save state for undo
            old_from_armies = from_territory.armies
            old_to_armies = to_territory.armies
            
            self.move_history.append({
                'action': 'move',
                'from_territory': from_territory,
                'to_territory': to_territory,
                'old_from_armies': old_from_armies,
                'old_to_armies': old_to_armies,
                'num_armies': num_armies
            })
            
            from_territory.armies -= num_armies
            to_territory.armies += num_armies
    
    def undo_move(self, move):
        """Undo the last move"""
        if not self.move_history:
            return
        
        last_move = self.move_history.pop()
        action = last_move['action']
        
        if action == 'place':
            territory = last_move['territory']
            territory.armies = last_move['old_armies']
            
        elif action == 'attack':
            from_territory = last_move['from_territory']
            to_territory = last_move['to_territory']
            old_owner = last_move['old_owner']
            
            from_territory.armies = last_move['old_from_armies']
            to_territory.armies = last_move['old_to_armies']
            
            # Restore ownership
            if to_territory.owner != old_owner:
                to_territory.owner.territories.remove(to_territory)
                to_territory.owner = old_owner
                if old_owner:
                    old_owner.territories.append(to_territory)
            
        elif action == 'move':
            from_territory = last_move['from_territory']
            to_territory = last_move['to_territory']
            
            from_territory.armies = last_move['old_from_armies']
            to_territory.armies = last_move['old_to_armies']
    
    def is_over(self):
        """Check if the game is over"""
        # Game is over if one player owns all territories
        all_owned_by_p1 = all(t.owner == self.player1 for t in self.territories.values() if t.owner is not None)
        all_owned_by_p2 = all(t.owner == self.player2 for t in self.territories.values() if t.owner is not None)
        
        return all_owned_by_p1 or all_owned_by_p2
    
    def get_winner(self):
        """Get the winner if game is over"""
        if not self.is_over():
            return None
        
        all_owned_by_p1 = all(t.owner == self.player1 for t in self.territories.values() if t.owner is not None)
        return self.player1 if all_owned_by_p1 else self.player2