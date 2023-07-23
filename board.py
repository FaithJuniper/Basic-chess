import pygame
import piece


class board:
    def __init__(self):
        self.squares = []
        self.white_figures = []
        self.black_figures = []
        self.selected_piece = None

    def draw_squares(self, window):
        pygame.draw.rect(window, (186, 140, 99), (40, 40, 400, 400))
        for row in range(8):
            for col in range(row % 2, 8, 2):
                pygame.draw.rect(window, (245, 245, 220), ((row * 50) + 40, (col * 50) + 40, 50, 50))
        pygame.draw.rect(window, (101, 78, 58), (35, 35, 410, 410), 5)

    def draw_pieces(self, window):
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
        self.draw_squares(window)
        for row in range(8):
            for col in range(8):
                piece = self.squares[row][col]
                piece.draw(window)

    def return_piece(self, row, col):
        return self.squares[row][col]

    def move(self, p1, p2):
        p2.colour = p1.colour
        p2.figure = p1.figure
        p2.picture = p1.picture
        p1.colour = "-"
        p1.figure = "-"
        p1.picture = "Pieces/BLANK.png"

    def calc_score(self):
        score = 0
        for fig in self.white_figures:
            score += fig.points
        for fig in self.black_figures:
            score += fig.points
        print(str(score))

    def reset_lists(self):
        self.white_figures.clear()
        self.black_figures.clear()
        for row in range(8):
            for col in range(8):
                current = self.squares[row][col]
                if current.colour == "W":
                    self.white_figures.append(current)
                elif current.colour == "B":
                    self.black_figures.append(current)

    def get_black(self):
        black = []
        for row in range(8):
            for col in range(8):
                temp = self.squares[row][col]
                if temp.colour == "B":
                    black.append(temp)
        return black

    def get_white(self):
        white = []
        for row in range(8):
            for col in range(8):
                temp = self.squares[row][col]
                if temp.colour == "W":
                    white.append(temp)
        return white
