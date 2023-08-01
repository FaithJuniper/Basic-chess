import sys
import legal

best_p1 = None
best_p2 = None
points = {
    "BP": -1,
    "BH": -3,
    "BB": -3,
    "BR": -5,
    "BQ": -10,
    "WP": 1,
    "WH": 3,
    "WB": 3,
    "WR": 5,
    "WQ": 10,
    "--": 0,
    "BK": 0,
    "WK": 0
}


def hint(board, turn):
    global best_p1, best_p2, points
    best_p1 = None
    best_p2 = None
    if turn:
        minimax_white(2, board, True, -sys.maxsize, sys.maxsize)
    else:
        minimax_black(2, board, True, -sys.maxsize, sys.maxsize)
    return best_p1, best_p2


def minimax_white(depth, board, cpu, alpha, beta):
    if depth == 0:
        return calc_score(board, True)
    elif cpu:
        max_value = -sys.maxsize
        for p1 in board.get_white():
            for row in board.squares:
                for p2 in row:
                    if legal.legal_move_white(p1, p2, board.squares):
                        temp_p1 = [p1.picture, p1.colour, p1.figure]
                        temp_p2 = [p2.picture, p2.colour, p2.figure]
                        board.move(p1, p2)
                        value = minimax_white(depth - 1, board, False, alpha, beta)
                        p1.picture, p1.colour, p1.figure = temp_p1[0], temp_p1[1], temp_p1[2]
                        p2.picture, p2.colour, p2.figure = temp_p2[0], temp_p2[1], temp_p2[2]
                        if value > max_value:
                            global best_p1, best_p2
                            best_p1 = p1
                            best_p2 = p2
                            max_value = max(value, max_value)
                        alpha = max(alpha, max_value)
                        if alpha >= beta:
                            break
                if alpha >= beta:
                    break
            if alpha >= beta:
                break
        return max_value
    else:
        min_value = sys.maxsize
        for p1 in board.get_black():
            for row in board.squares:
                for p2 in row:
                    if legal.legal_move_black(p1, p2, board.squares):
                        temp_p1 = [p1.picture, p1.colour, p1.figure]
                        temp_p2 = [p2.picture, p2.colour, p2.figure]
                        board.move(p1, p2)
                        value = minimax_white(depth - 1, board, True, alpha, beta)
                        p1.picture, p1.colour, p1.figure = temp_p1[0], temp_p1[1], temp_p1[2]
                        p2.picture, p2.colour, p2.figure = temp_p2[0], temp_p2[1], temp_p2[2]
                        min_value = min(value, min_value)
                        beta = min(beta, min_value)
                        if alpha >= beta:
                            break
                if alpha >= beta:
                    break
            if alpha >= beta:
                break
        return min_value


def minimax_black(depth, board, cpu, alpha, beta):
    if depth == 0:
        return calc_score(board, False)
    elif cpu:
        max_value = -sys.maxsize
        for p1 in board.get_black():
            for row in board.squares:
                for p2 in row:
                    if legal.legal_move_black(p1, p2, board.squares):
                        temp_p1 = [p1.picture, p1.colour, p1.figure]
                        temp_p2 = [p2.picture, p2.colour, p2.figure]
                        board.move(p1, p2)
                        value = minimax_black(depth - 1, board, False, alpha, beta)
                        p1.picture, p1.colour, p1.figure = temp_p1[0], temp_p1[1], temp_p1[2]
                        p2.picture, p2.colour, p2.figure = temp_p2[0], temp_p2[1], temp_p2[2]
                        if value > max_value:
                            global best_p1, best_p2
                            best_p1 = p1
                            best_p2 = p2
                            max_value = max(value, max_value)
                        alpha = max(alpha, max_value)
                        if alpha >= beta:
                            break
                if alpha >= beta:
                    break
            if alpha >= beta:
                break
        return max_value
    else:
        min_value = sys.maxsize
        for p1 in board.get_white():
            for row in board.squares:
                for p2 in row:
                    if legal.legal_move_white(p1, p2, board.squares):
                        temp_p1 = [p1.picture, p1.colour, p1.figure]
                        temp_p2 = [p2.picture, p2.colour, p2.figure]
                        board.move(p1, p2)
                        value = minimax_black(depth - 1, board, True, alpha, beta)
                        p1.picture, p1.colour, p1.figure = temp_p1[0], temp_p1[1], temp_p1[2]
                        p2.picture, p2.colour, p2.figure = temp_p2[0], temp_p2[1], temp_p2[2]
                        min_value = min(value, min_value)
                        beta = min(beta, min_value)
                        if alpha >= beta:
                            break
                if alpha >= beta:
                    break
            if alpha >= beta:
                break
        return min_value


def calc_score(board, turn):
    score = 0
    if turn:
        for row in board.squares:
            for p2 in row:
                score += points[p2.colour + p2.figure]
    else:
        for row in board.squares:
            for p2 in row:
                score += -(points[p2.colour + p2.figure])
    return score
