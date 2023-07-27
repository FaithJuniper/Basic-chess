import pygame

import piece
import legal


class board:
    def __init__(self):
        self.squares = []
        self.white_figures = []
        self.black_figures = []
        self.selected_piece = None
        self.server = None

    def set_server(self, server):
        self.server = server

    def draw_squares(self, window):
        # Draws the main layout of the chess board
        pygame.draw.rect(window, (186, 140, 99), (40, 40, 400, 400))
        for row in range(8):
            for col in range(row % 2, 8, 2):
                pygame.draw.rect(window, (245, 245, 220), ((row * 50) + 40, (col * 50) + 40, 50, 50))
        pygame.draw.rect(window, (101, 78, 58), (35, 35, 410, 410), 5)

    def draw_pieces(self, window):
        # Creates chess piece objects and draws them on the board
        for row in range(8):
            self.squares.append([])
            for col in range(8):
                if row < 2:
                    p = piece.piece(row, col)
                    self.squares[row].append(p)
                    self.black_figures.append(p)
                    self.squares[row][col].draw(window)
                elif row > 5:
                    p = piece.piece(row, col)
                    self.squares[row].append(p)
                    self.white_figures.append(p)
                    self.squares[row][col].draw(window)
                else:
                    p = piece.piece(row, col)
                    self.squares[row].append(p)
                    self.squares[row][col].draw(window)

    def draw(self, window):
        # Updates chess board
        self.draw_squares(window)
        for row in range(8):
            for col in range(8):
                piece = self.squares[row][col]
                piece.draw(window)

    def click(self):
        x, y = pygame.mouse.get_pos()
        if (40 < x < 440) and (40 < y < 440):
            col = (x - 40) // 50
            row = (y - 40) // 50
            piece = self.squares[row][col]
            if self.selected_piece is None:
                # Selects a piece
                self.selected_piece = piece
                print("SELECTED")
            elif piece == self.selected_piece:
                # Unselects a piece
                self.selected_piece = None
                print("UNSELECTED")
            else:
                # Moves selected piece to a new space
                if legal.legal_move_white(self.selected_piece, piece, self.squares):
                    print("CORRECT MOVE")
                    self.move(self.selected_piece, piece)
                    self.server.send_message("##" + str(self.selected_piece.row) + str(self.selected_piece.col)
                                             + str(piece.row) + str(piece.col))
                self.selected_piece = None

    def move(self, p1, p2):
        # Changes over piece attributes
        p2.colour = p1.colour
        p2.figure = p1.figure
        p2.picture = p1.picture
        p1.colour = "-"
        p1.figure = "-"
        p1.picture = "Pieces/BLANK.png"

    def calc_score(self):
        # Calculates overall score
        score = 0
        for fig in self.white_figures:
            score += fig.points
        for fig in self.black_figures:
            score += fig.points
        print(str(score))

    def get_black(self):
        # Gets all black pieces on the board
        black = []
        for row in range(8):
            for col in range(8):
                temp = self.squares[row][col]
                if temp.colour == "B":
                    black.append(temp)
        return black

    def get_white(self):
        # Gets all white pieces on the board
        white = []
        for row in range(8):
            for col in range(8):
                temp = self.squares[row][col]
                if temp.colour == "W":
                    white.append(temp)
        return white
