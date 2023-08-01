import pygame
import piece
import legal
import minimax


class board:
    def __init__(self):
        self.squares = []
        self.white_figures = []
        self.black_figures = []
        self.selected_piece = None
        self.game_started = False
        self.turn = True
        self.highlighted = {}

    def draw_squares(self, window):
        # Draws the main layout of the chess board
        pygame.draw.rect(window, (186, 140, 99), (40, 40, 400, 400))
        for row in range(8):
            for col in range(row % 2, 8, 2):
                pygame.draw.rect(window, (245, 245, 220), ((row * 50) + 40, (col * 50) + 40, 50, 50))
        pygame.draw.rect(window, (101, 78, 58), (35, 35, 410, 410), 5)
        for col, row in self.highlighted:
            pygame.draw.rect(window, self.highlighted[(col, row)], ((col*50)+40, (row*50)+40, 50, 50))

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
        if self.game_started and (40 < x < 440) and (40 < y < 440):
            col = (x - 40) // 50
            row = (y - 40) // 50
            piece = self.squares[row][col]
            if self.selected_piece is None:
                # Selects a piece
                self.selected_piece = piece
                self.highlighted[(col, row)] = (165, 42, 42)
            else:
                # If move is valid, moves selected piece to new spot
                if self.turn and legal.legal_move_white(self.selected_piece, piece, self.squares):
                    self.move(self.selected_piece, piece)
                    self.turn = False
                    self.highlighted.clear()
                elif (not self.turn) and legal.legal_move_black(self.selected_piece, piece, self.squares):
                    self.move(self.selected_piece, piece)
                    self.turn = True
                    self.highlighted.clear()
                else:
                    self.highlighted.pop((self.selected_piece.col, self.selected_piece.row))
                    self.selected_piece = None
                self.selected_piece = None

    def find_hint(self):
        p1, p2 = minimax.hint(self, self.turn)
        self.highlighted[(p1.col, p1.row)] = (192, 87, 87)
        self.highlighted[(p2.col, p2.row)] = (192, 87, 87)

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
