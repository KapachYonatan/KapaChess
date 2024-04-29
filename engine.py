import chess
import chess.polyglot
from MCST.mcts import mcts
from MCST.node import Node


class ChessEngine:
    def __init__(self, board):
        self.board = board
        self.is_opening = True

    def get_best_move(self):
        if self.is_opening:
            opening_move = self.select_opening_move()
            if opening_move is None:
                self.is_opening = False
            else:
                return opening_move.uci()
        #legal_moves = list(self.board.legal_moves)
        #return random.choice(legal_moves).uci() if legal_moves else None
        root = Node(self.board)
        return mcts(root, 500).uci()

    def select_opening_move(self):
        with chess.polyglot.open_reader("baronbook30/baron30.bin") as reader:
            try:
                entry = reader.choice(self.board)  # Chooses a move based on the position
                return entry.move
            except IndexError:
                # No valid move found in the opening book, you need to handle it
                return None