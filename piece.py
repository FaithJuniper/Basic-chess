import pygame


class piece:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.colour = ""
        self.figure = ""
        self.picture = ""
        if self.row == 0 and (self.col == 0 or self.col == 7):
            self.picture = "Pieces/BR.png"
            self.colour = "B"
            self.figure = "R"
        elif self.row == 0 and (self.col == 1 or self.col == 6):
            self.picture = "Pieces/BH.png"
            self.colour = "B"
            self.figure = "H"
        elif self.row == 0 and (self.col == 2 or self.col == 5):
            self.picture = "Pieces/BB.png"
            self.colour = "B"
            self.figure = "B"
        elif self.row == 0 and self.col == 3:
            self.picture = "Pieces/BQ.png"
            self.colour = "B"
            self.figure = "Q"
        elif self.row == 0 and self.col == 4:
            self.picture = "Pieces/BK.png"
            self.colour = "B"
            self.figure = "K"
        elif self.row == 1:
            self.picture = "Pieces/BP.png"
            self.colour = "B"
            self.figure = "P"
        elif self.row == 7 and (self.col == 0 or self.col == 7):
            self.picture = "Pieces/WR.png"
            self.colour = "W"
            self.figure = "R"
        elif self.row == 7 and (self.col == 1 or self.col == 6):
            self.picture = "Pieces/WH.png"
            self.colour = "W"
            self.figure = "H"
        elif self.row == 7 and (self.col == 2 or self.col == 5):
            self.picture = "Pieces/WB.png"
            self.colour = "W"
            self.figure = "B"
        elif self.row == 7 and self.col == 3:
            self.picture = "Pieces/WQ.png"
            self.colour = "W"
            self.figure = "Q"
        elif self.row == 7 and self.col == 4:
            self.picture = "Pieces/WK.png"
            self.colour = "W"
            self.figure = "K"
        elif self.row == 6:
            self.picture = "Pieces/WP.png"
            self.colour = "W"
            self.figure = "P"
        else:
            self.picture = "Pieces/BLANK.png"
            self.colour = "-"
            self.figure = "-"

        self.x = 0
        self.y = 0

    def set_pos(self):
        self.x = (50 * self.col) + 40
        self.y = (50 * self.row) + 40

    def move(self, row, col):
        self.row = row
        self.col = col
        self.set_pos()

    def draw(self, window):
        pic = pygame.transform.scale(pygame.image.load(self.picture), (50, 50))
        window.blit(pic, ((self.col * 50) + 40, (self.row * 50) + 40))