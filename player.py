from board import Direction, Rotation, Action
from random import Random
import time


class Player:
    def __init__(self, seed=None):
        self.random = Random(seed)

    def print_board(self, board):
        print("--------")
        for y in range(24):
            s = ""
            for x in range(10):
                if (x,y) in board.cells:
                    s += "#"
                else:
                    s += "."
            print(s, y)

    def bound_by_left(self, board):#could decide when to activate 9 col method
        left_bound_score = 0
        '''check_range = 0
        if self.len_check == 9:
            check_range = 8
        elif self.len_check == 10:
            check_range = 9'''
        for y in range(24):#could be optimised further
            for x in range(0, 9):#swap 9 to check range later
                if (x, y) in board.cells:
                    if (x + 1, y) not in board.cells:
                        left_bound_score += abs(y - 24) ** self.side_polynomial
        return left_bound_score

    def bound_by_right(self, board):
        right_bound_score = 0
        for y in range(24):
            for x in range(1, 10):
                if (x, y) in board.cells:
                    if (x - 1, y) not in board.cells:
                        right_bound_score += abs(y - 24) ** self.side_polynomial
        return right_bound_score

    def bound_by_top(self, board):
        top_bound_score = 0
        for y in range(24):
            for x in range(10):
                if (x, y) in board.cells:
                    for yi in range(0, y, -1):
                        if (x, yi) not in board.cells:
                            hole_score += abs(y - 24) ** self.top_polynomial
        return top_bound_score



class RandomPlayer(Player):
    def __init__(self, seed=None):
        self.random = Random(seed)

    def print_board(self, board):
        print("--------")
        for y in range(24):
            s = ""
            for x in range(10):
                if (x,y) in board.cells:
                    s += "#"
                else:
                    s += "."
            print(s, y)
                

            

    def choose_action(self, board):
        self.print_board(board)
        time.sleep(0.5)
        if self.random.random() > 0.97:
            # 3% chance we'll discard or drop a bomb
            return self.random.choice([
                Action.Discard,
                Action.Bomb,
            ])
        else:
            # 97% chance we'll make a normal move
            return self.random.choice([
                Direction.Left,
                Direction.Right,
                Direction.Down,
                Rotation.Anticlockwise,
                Rotation.Clockwise,
            ])


SelectedPlayer = Player

