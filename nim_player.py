import math
import random
from copy import deepcopy

class Player():
    def __init__(self):
        self.player = self.__class__.__name__

class Player():
    def __init__(self, player):
        self.alias = player
    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, player):
        self.alias = player
        # super().__init__(player) 
        

    def get_move(self, game):
        valid_stone_number = False
        val = None
        while not valid_stone_number:
            user_input = input(self.alias + '\'s turn. Input move (0-9): ')
            try:
                val = int(user_input)
                if (val not in [1,2,3]) & (val not in game.available_moves()):
                    raise ValueError
                valid_stone_number = True
            except ValueError:
                print('Invalid stone number. Try again.')
        return val


class RandomPlayer(Player):
    def __init__(self, player):
        self.alias = player  

    def get_move(self, game):
        move = random.choice(game.available_moves())
        return move


class AI(Player):
    def __init__(self, player):
        self.alias = player

    def get_move(self, game):
        move = self.choose_move(deepcopy(game)) 
        return move

    def choose_move(self, game):
        move =  minimax(game)
        return move


def minimax(game):
    MAX, MIN = 1000, -1000 

    def internal(move , game, maximizingPlayer, alpha, beta):
        # Terminating condition. i.e 
        if not game.possible_states():
            print(str(move) + '|' + str(game)+ '|' + str(maximizingPlayer) )
            return move
        if maximizingPlayer:
            best = MIN 
            for move, state in game.possible_states().items(): #possible state is a dictionnary {move1: state1, move2; state2}
                val = internal(move , state, False, alpha, beta) 
                best = max(best, val) 
                alpha = max(alpha, best) 
                # Alpha Beta Pruning 
                if beta <= alpha: 
                    break 
            return best 
        else:
            best = MAX 
            for move, state in game.possible_states().items(): 
                val = internal(move , state, True, alpha, beta) 
                best = min(best, val) 
                beta = min(beta, best) 
                # Alpha Beta Pruning 
                if beta <= alpha: 
                    break 
            return best 

    best_move = internal(None , game, True, MIN, MAX)
    return best_move