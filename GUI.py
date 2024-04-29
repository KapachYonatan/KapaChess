import PySimpleGUI as sg
import chess

pieces_path = "img/"


def get_curr_layout(board):
    board_layout = []
    for i in range(8):
        row = []
        for j in range(8):
            piece = board.piece_at(chess.square(j, 7 - i))
            piece_image = '' if piece is None else pieces_path + f"{('w_' if piece.color == chess.WHITE else 'b_')}{piece.symbol().lower()}.png"
            button = sg.Button('', size=(6, 3), key=(7 - i, j), pad=(0, 0),
                               image_filename=piece_image, image_size=(51.5, 51.5),
                               button_color=('white', 'gray' if (i + j) % 2 == 0 else 'dark gray'),
                               border_width=0)
            row.append(button)
        board_layout.append(row)
    return board_layout


def create_chess_gui(chess_logic):
    sg.theme('DarkGreen4')
    layout = get_curr_layout(chess_logic.board)
    window = sg.Window('Chess', layout, finalize=True)
    return window


def update_gui(window, board):
    # Redraw the entire board or just update changed squares
    for i in range(8):
        for j in range(8):
            piece = board.piece_at(chess.square(j, 7-i))
            piece_image = '' if not piece else pieces_path + f"{('w_' if piece.color == chess.WHITE else 'b_')}{piece.symbol().lower()}.png"
            window[(7-i, j)].update(image_filename=piece_image, image_size=(51.5, 51.5))
