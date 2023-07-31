
def legal_move_white(p1, p2, squares):
    if p1 == p2:
        return False
    if p1.colour == "W" and (p2.colour != "W"):
        # PAWN
        if p1.figure == "P":
            if p2.colour == "-":
                if (p1.col == p2.col and p1.row == p2.row + 1) or ((p1.col == p2.col and p1.row == p2.row + 2)
                                                                   and p1.row == 6):
                    if interfere(p1, p2, squares):
                        return True
            else:
                if p1.row == p2.row + 1 and (p1.col == p2.col + 1 or p1.col == p2.col - 1):
                    return True
        # HORSE
        if p1.figure == "H":
            if (abs(p1.col - p2.col) == 2 and abs(p1.row - p2.row) == 1) or (
                    abs(p1.col - p2.col) == 1 and abs(p1.row - p2.row) == 2):
                return True
        # KING
        if p1.figure == "K":
            if abs(p1.col - p2.col) <= 1 and abs(p1.row - p2.row) <= 1:
                return True
        # ROOK
        if p1.figure == "R":
            if p1.col == p2.col or p1.row == p2.row:
                if interfere(p1, p2, squares):
                    return True
        # BISHOP
        if p1.figure == "B":
            if abs(p1.col - p2.col) == abs(p1.row - p2.row):
                if interfere(p1, p2, squares):
                    return True
        # QUEEN
        if p1.figure == "Q":
            if abs(p1.col - p2.col) == abs(p1.row - p2.row) or (p1.col == p2.col or p1.row == p2.row):
                if interfere(p1, p2, squares):
                    return True


def legal_move_black(p1, p2, squares):
    if p1 == p2:
        return False
    if p1.colour == "B" and p2.colour != "B":
        # PAWN
        if p1.figure == "P":
            if p2.colour == "-":
                if (p1.col == p2.col and p1.row == p2.row - 1) or ((p1.col == p2.col and p1.row == p2.row - 2)
                                                                   and p1.row == 1):
                    if interfere(p1, p2, squares):
                        return True
            else:
                if p1.row == p2.row - 1 and (p1.col == p2.col + 1 or p1.col == p2.col - 1):
                    return True
        # HORSE
        if p1.figure == "H":
            if (abs(p1.col - p2.col) == 2 and abs(p1.row - p2.row) == 1) or (
                    abs(p1.col - p2.col) == 1 and abs(p1.row - p2.row) == 2):
                return True
        # KING
        if p1.figure == "K":
            if abs(p1.col - p2.col) <= 1 and abs(p1.row - p2.row) <= 1:
                return True
        # ROOK
        if p1.figure == "R":
            if p1.col == p2.col or p1.row == p2.row:
                if interfere(p1, p2, squares):
                    return True
        # BISHOP
        if p1.figure == "B":
            if abs(p1.col - p2.col) == abs(p1.row - p2.row):
                if interfere(p1, p2, squares):
                    return True
        # QUEEN
        if p1.figure == "Q":
            if abs(p1.col - p2.col) == abs(p1.row - p2.row) or (p1.col == p2.col or p1.row == p2.row):
                if interfere(p1, p2, squares):
                    return True


def interfere(p1, p2, squares):
    if p1.row == p2.row:
        mini = min(p1.col, p2.col) + 1
        maxi = max(p1.col, p2.col)
        for hyp_col in range(mini, maxi):
            if squares[p2.row][hyp_col].colour != "-":
                return False
        return True
    elif p1.col == p2.col:
        mini = min(p1.row, p2.row) + 1
        maxi = max(p1.row, p2.row)
        for hyp_row in range(mini, maxi):
            if squares[hyp_row][p2.col].colour != "-":
                return False
        return True
    else:
        if p2.row < p1.row and p2.col < p1.col:
            min_row, max_row = p2.row + 1, p1.row
            hyp_col, col_inc = p2.col + 1, 1
        elif p2.row > p1.row and p2.col < p1.col:
            min_row, max_row = p1.row + 1, p2.row
            hyp_col, col_inc = p1.col - 1, -1
        elif p2.row < p1.row and p2.col > p1.col:
            min_row, max_row = p2.row + 1, p1.row
            hyp_col, col_inc = p2.col - 1, -1
        else:
            min_row, max_row = p1.row + 1, p2.row
            hyp_col, col_inc = p1.col + 1, 1
        for hyp_row in range(min_row, max_row):
            if squares[hyp_row][hyp_col].colour != "-":
                return False
            hyp_col += col_inc
        return True
