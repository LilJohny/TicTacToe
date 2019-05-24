from board import Board
from binary_search_tree import BSTree
import copy
import random


class Opponent:
    def __init__(self, board):
        self._board = board

    def make_move(self):
        tree = BSTree()

        def _move_helper(board, tree):
            possible_moves = board.get_possible_moves()
            lcopy = copy.deepcopy(board)
            rcopy = copy.deepcopy(board)

            if len(possible_moves) > 1:
                lmove = random.choice(possible_moves)
                possible_moves.remove(lmove)
                rmove = random.choice(possible_moves)
                board.last_move = -board.last_move
                lcopy.make_move(lmove, board.last_move)
                rcopy.make_move(rmove, board.last_move)
                tree.left = lcopy
                tree.right = rcopy
                _move_helper(lcopy, tree.left)
                _move_helper(rcopy, tree.right)
            elif len(possible_moves) == 1:
                lcopy.make_move(possible_moves[0], self._board.last_move)
                rcopy.make_move(possible_moves[0], self._board.last_move)
                tree.left = lcopy
                tree.right = rcopy
                return None
            else:
                return None

        _move_helper(self._board, tree)
        left_subtree = tree.left.get_leafs()
        left_score = self.score(left_subtree)
        right_subtree = tree.right.get_leafs()
        right_score = self.score(right_subtree)
        if left_score > right_score:
            return tree.left
        elif right_score > left_score:
            return tree.right
        else:
            return random.choice([tree.left, tree.right])

    def score(self, leafs):
        tree_score = 0
        for leaf in leafs:
            if leaf.data.has_winner() == 1:
                tree_score += 1
            elif leaf.data.has_winner() == -1:
                tree_score -= 1
        return tree_score


def main():
    board = Board()
    print("Starting game...")
    print(board)
    print("To make moves you can choose two indices frm 1 to 3:")
    while not board.has_winner():
        print(board)
        print("Make your move:")
        move = input("Type your move in format XxY: ")
        while not (len(move.split("x")) != 2 and  all(
                map(lambda x: x.isdigit() and 1 <= int(x) <= 3, move.split("x")))):
            print("You entered wrong move")
            move = input("Type your move in format XxY: ")
        x, y = list(map(int, move.split("x")))
        board.last_move = 1
        board_move = board.make_move((y - 1, x - 1))
        while not board_move:
            print("You entered wrong move")
            move = input("Type your move in format XxY: ")
            x, y = list(map(int, move.split("x")))
            board.last_move = 1
            board_move = board.make_move((y - 1, x - 1))
        print(board)
        print("Computer`s turn: ")
        opponent = Opponent(board)
        board = opponent.make_move().data


if __name__ == "__main__":
    main()
