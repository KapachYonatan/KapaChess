import math


def ucb1_formula(node, log_visits):
    if node.visits == 0:
        return 0
    else:
        return node.wins / node.visits + math.sqrt(2 * log_visits / node.visits)


class Node:
    def __init__(self, board, move=None, parent=None):
        self.board = board
        self.move = move
        self.parent = parent
        self.children = []
        self.wins = 0
        self.visits = 0
        self.unexplored_moves = list(board.legal_moves)

    def is_fully_expanded(self):
        return len(self.unexplored_moves) == 0

    def add_child(self):
        move = self.unexplored_moves.pop()
        new_board = self.board.copy()
        new_board.push(move)
        child_node = Node(new_board, move, self)
        self.children.append(child_node)
        return child_node

    def update(self, result):
        self.visits += 1
        self.wins += result

    def select_child(self):
        # Using the UCB1 formula for selection
        log_visits = math.log(self.visits)
        return max(self.children, key=lambda x: ucb1_formula(x, log_visits))

