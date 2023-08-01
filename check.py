import legal


def checkmate_white(board):
    # Checks whether white king is in checkmate
    in_checkmate = True
    for p1 in board.get_white():
        for row in board.squares:
            for p2 in row:
                if legal.legal_move_white(p1, p2, board.squares):
                    temp_p1 = [p1.picture, p1.colour, p1.figure]
                    temp_p2 = [p2.picture, p2.colour, p2.figure]
                    move(p1, p2)
                    if not check_white(board):
                        in_checkmate = False
                    p1.picture, p1.colour, p1.figure = temp_p1[0], temp_p1[1], temp_p1[2]
                    p2.picture, p2.colour, p2.figure = temp_p2[0], temp_p2[1], temp_p2[2]
    return in_checkmate


def checkmate_black(board):
    # Checks whether white king is in checkmate
    in_checkmate = True
    for p1 in board.get_black():
        for row in board.squares:
            for p2 in row:
                if legal.legal_move_black(p1, p2, board.squares):
                    temp_p1 = [p1.picture, p1.colour, p1.figure]
                    temp_p2 = [p2.picture, p2.colour, p2.figure]
                    move(p1, p2)
                    if not check_black(board):
                        in_checkmate = False
                    p1.picture, p1.colour, p1.figure = temp_p1[0], temp_p1[1], temp_p1[2]
                    p2.picture, p2.colour, p2.figure = temp_p2[0], temp_p2[1], temp_p2[2]
    return in_checkmate


def check_white(board):
    # Checks whether the white king is in check
    for p1 in board.get_black():
        for row in board.squares:
            for p2 in row:
                if p2.figure == "K" and p2.colour == "W" and legal.legal_move_black(p1, p2, board.squares):
                    return True


def check_black(board):
    # Checks whether the black king is in check
    for p1 in board.get_white():
        for row in board.squares:
            for p2 in row:
                if p2.figure == "K" and p2.colour == "B" and legal.legal_move_white(p1, p2, board.squares):
                    return True


def white_valid(board, p1, p2):
    # Checks if white move still leaves king in check
    safe = False
    temp_p1 = [p1.picture, p1.colour, p1.figure]
    temp_p2 = [p2.picture, p2.colour, p2.figure]
    move(p1, p2)
    if not check_white(board):
        safe = True
    p1.picture, p1.colour, p1.figure = temp_p1[0], temp_p1[1], temp_p1[2]
    p2.picture, p2.colour, p2.figure = temp_p2[0], temp_p2[1], temp_p2[2]
    return safe


def black_valid(board, p1, p2):
    # Checks if black move still leaves king in check
    safe = False
    temp_p1 = [p1.picture, p1.colour, p1.figure]
    temp_p2 = [p2.picture, p2.colour, p2.figure]
    move(p1, p2)
    if not check_black(board):
        safe = True
    p1.picture, p1.colour, p1.figure = temp_p1[0], temp_p1[1], temp_p1[2]
    p2.picture, p2.colour, p2.figure = temp_p2[0], temp_p2[1], temp_p2[2]
    return safe


def move(p1, p2):
    # Changes over piece attributes
    p2.colour = p1.colour
    p2.figure = p1.figure
    p2.picture = p1.picture
    p1.colour = "-"
    p1.figure = "-"
    p1.picture = "Pieces/BLANK.png"
