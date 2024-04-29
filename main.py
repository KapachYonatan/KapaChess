from game_logic import ChessLogic
from engine import ChessEngine
from GUI import create_chess_gui
from GUI import update_gui
import PySimpleGUI as sg
import chess


def main():
    # Initialize the game logic, engine and GUI
    chess_logic = ChessLogic()
    chess_engine = ChessEngine(chess_logic.board)
    window = create_chess_gui(chess_logic)

    # Function to handle AI's move out of opening phase
    def handle_ai_move():
        ai_move = chess_engine.get_best_move()
        if ai_move:
            print(ai_move)
            chess_logic.make_move(ai_move)
            update_gui(window, chess_logic.board)
            return ai_move
        return None

    source_square = None

    while True:
        player_turn = True
        while player_turn:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                window.close()
            if isinstance(event, tuple):  # User makes a move
                print(f"Received click at: {event}")  # Debugging output
                if source_square:
                    source_index = chess.square(source_square[1], source_square[0])
                    destination_index = chess.square(event[1], event[0])
                    move = chess.Move(source_index, destination_index)
                    move_uci = move.uci()  # Convert move to UCI format
                    print(f"Constructed move: {move_uci}")  # Debugging output
                    if chess_logic.make_move(move_uci):
                        update_gui(window, chess_logic.board)
                        print(f"Move successful. Current game status: {chess_logic.game_status()}")
                        player_turn = False
                    else:
                        print("Invalid move")
                    source_square = None
                else:
                    source_square = event
        handle_ai_move()


if __name__ == "__main__":
    main()