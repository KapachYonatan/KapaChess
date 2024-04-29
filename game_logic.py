import chess


class ChessLogic:
    def __init__(self):
        self.board = chess.Board()

    def is_move_legal(self, move):
        try:
            chess_move = chess.Move.from_uci(move)
            return chess_move in self.board.legal_moves
        except:
            return False

    def make_move(self, move):
        if self.is_move_legal(move):
            self.board.push(chess.Move.from_uci(move))
            return True
        return False

    def game_status(self):
        if self.board.is_checkmate():
            return "Checkmate"
        if self.board.is_stalemate():
            return "Stalemate"
        return "Continue"
