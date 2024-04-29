import random


def mcts(root, iterations=1000):
    for i in range(iterations):
        # print(f"Starting sim {i}")
        node = root
        # Selection
        while node.is_fully_expanded() and node.children:
            # print("Node fully expanded, selecting child")
            node = node.select_child()

        # Expansion
        if not node.is_fully_expanded():
            # print("Expanding, adding child")
            node = node.add_child()

        # Simulation
        # print("Simulating a game")
        result = simulate_random_game(node.board)

        # Backpropagation
        while node is not None:
            node.update(result)
            node = node.parent

    # Select the best move from the root
    best_child = max(root.children, key=lambda x: x.visits)
    return best_child.move


def simulate_random_game(board):
    simulation_board = board.copy()
    while not simulation_board.is_game_over():
        # print("Making random move")
        move = random.choice(list(simulation_board.legal_moves))
        simulation_board.push(move)
    # Define how to calculate the result (1 win, 0 loss, 0.5 draw)
    result = 0 if simulation_board.result() == '0-1' else 1 if simulation_board.result() == '1-0' else 0.5
    return result
