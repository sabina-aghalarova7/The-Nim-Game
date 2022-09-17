import math
import time
from nim_player import HumanPlayer, RandomPlayer, AI

class Game():
    def __init__(self, default_stone_count):
        self.default_stone_count = default_stone_count

class Nim(Game):
    def __init__(self, default_stone_count):
        self.default_stone_count = default_stone_count
        self.stones = self.create_stones(self.default_stone_count)
        self.current_winner = None
        self.player = None
        self.score = 0
    @staticmethod
    def create_stones(n):
        return list(range(1,n))

    def print_position(self):
        print(self.stones)

    def print_available_moves(self):
        if len(self.stones) > 3:
            print([1,2,3])
        else:
            print(self.stones)

    def available_moves(self):
        if len(self.stones) > 3:
            available_moves = [1,2,3]
        elif len(self.stones) == 3:
            available_moves = [1,2,3]
        elif len(self.stones) == 2:
            available_moves = [1,2]
        elif len(self.stones) == 1:
            available_moves = [1]
        else:
            available_moves = []
        print(f'available_moves: {available_moves}')
        return(available_moves)         

    def number_of_available_moves(self):
        return len(self.available_moves)

    def possible_states(self):
        games = {}
        for move in self.available_moves():
            games[move] = Nim(len(self.stones)-move)
        return games

    def make_move(self, move, player):
        self.stones = self.stones[:len(self.stones)-move]
        if self.winner():
            self.current_winner = player

    def winner(self):
        if not self.available_moves():
            return True
        else:
            return False

def play(game, Player1, Player2, print_game=True):
    move = Player1.get_move(game)

    # print(game.possible_states())
    if game.current_winner:
        print(game.current_winner.alias + ' wins!')
        return f'{game.current_winner.alias} wins'
    else:
        move = Player1.get_move(game)
        game.make_move(move, Player1)
        if print_game:
            print(Player1.alias + f' drops {move} stones')
            game.print_position()
        play(game, Player2, Player1, print_game=True)





