#Код Олеся Мар'яновича з консультації

import random

def generate_winning_combinations():
    """Function generates all wining combinations for tictactoe board
    
    Returns:
        list: All wining combinations
    """
    combinations = []
    for i in range(3):
        combination1 = []
        combination2 = []
        for j in range(3):
            combination1.append((i, j))
            combination2.append((j, i))
        combinations.append(combination1)
        combinations.append(combination2)

    combinations.append([(0, 0), (1, 1), (2, 2)])
    combinations.append([(0, 2), (1, 1), (2, 0)])
    return combinations

class Board:
    """Class representing tictactoe board"""
    NOUGHT = 1
    CROSS = -1
    EMPTY = 0

    NOUGHT_WINNER = 1
    CROSS_WINNER = -1
    DRAW = 2
    NOT_FINISHED = 0

    WINNING_COMBINATIONS = generate_winning_combinations()

    def __init__(self):
        """Method initializes new instance of Board class
        """
        self.cells = [[0] * 3 for _ in range(3)]
        self.last_move = Board.NOUGHT
        self.number_of_moves = 0


    def make_move(self, cell, last_move=None):
        """Method makes move for given positions
        
        Args:
            cell (tuple): Coordinates 
            last_move (int, optional): 1 for player, -1 for computer. Defaults to None.
        
        Returns:
            bool: True if move was successful else False
        """
        if self.cells[cell[0]][cell[1]] != 0:
            return False
        self.last_move = -self.last_move if last_move is  None else last_move
        self.cells[cell[0]][cell[1]] = self.last_move
        self.number_of_moves += 1
        return True

    def has_winner(self):
       for combination in self.WINNING_COMBINATIONS:
            lst = []
            for cell in combination:
                lst.append(self.cells[cell[0]][cell[1]])
            if max(lst) == min(lst) and max(lst) != Board.EMPTY:
                return max(lst)
       if self.number_of_moves == 9:
           return Board.DRAW

       return Board.NOT_FINISHED


    def get_possible_moves(self):
        """Method gets all possible moves for current state of board
        
        Returns:
            list: List of all possible moves
        """
        possible_moves = []
        for i in range(3):
            for j in range(3):
                if self.cells[i][j] == Board.EMPTY:
                    possible_moves.append((i, j))
        return possible_moves

    def get_random_move(self):
        """Method gets random move for current state of board
        
        Returns:
            tuple: Coordinates for random move
        """
        possible_moves = self.get_possible_moves()
        cell = random.choice(possible_moves)
        return cell

    def __str__(self):
        transform = {0: " ", 1: "O", -1:"X"}
        return "\n".join([" ".join(map(lambda x: transform[x], row)) for row in self.cells])


