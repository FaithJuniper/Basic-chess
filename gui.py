import pygame


class gui:
    def __init__(self):
        pygame.font.init()

        # The base rectangles of buttons
        self.create_rect = None
        self.hint_rect = None
        self.tick_box = None

        # Game stats
        self.game_started = False
        self.hints = False

        # Font styles
        self.title_font = pygame.font.Font(None, 32)
        self.writing_font = pygame.font.Font(None, 22)

    def draw_menu(self, window):
        # Draws background
        window.fill((53, 101, 77))
        for y in range(480):
            if y % 10 == 0:
                for x in range(743):
                    if x % 10 == 0:
                        pygame.draw.rect(window, (48, 91, 71), (x, y, 5, 5))
        pygame.draw.rect(window, (42, 81, 62), (0, 0, 743, 480), 10)
        pygame.draw.rect(window, (27, 52, 40), (0, 0, 743, 480), 3)

        # Draws menu
        pygame.draw.rect(window, (245, 245, 220), (480, 40, 223, 70))
        pygame.draw.rect(window, (101, 78, 58), (475, 35, 233, 80), 5)

        # Adds 'buttons'
        self.create_rect = pygame.draw.rect(window, (186, 140, 99), (625, 57, 60, 30))
        pygame.draw.rect(window, (101, 78, 58), (622, 54, 66, 36), 3)
        button_text2 = self.writing_font.render("Start", True, (0, 0, 0))
        window.blit(button_text2, (634, 65))
        self.tick_box = pygame.draw.rect(window, (245, 245, 220), (592, 83, 11, 11))
        pygame.draw.rect(window, (101, 78, 58), (590, 81, 15, 15), 2)

        # Adds text
        title1 = self.title_font.render("New Game", True, (0, 0, 0))
        window.blit(title1, (490, 50))
        words1a = self.writing_font.render("Allow hints?", True, (0, 0, 0))
        window.blit(words1a, (490, 82))

    def click(self, window):
        pos = pygame.mouse.get_pos()

        if self.game_started:
            if self.hints and self.hint_rect.collidepoint(pos):
                return "hint"
        else:
            # Starts game
            if self.create_rect.collidepoint(pos):
                pygame.draw.rect(window, (53, 101, 77), (475, 35, 250, 155))
                for y in range(480):
                    if y % 10 == 0:
                        for x in range(760):
                            if x % 10 == 0 and ((475 < x < 725) and (35 < y < 190)):
                                pygame.draw.rect(window, (48, 91, 71), (x, y, 5, 5))

                # Draws turn indicator
                pygame.draw.rect(window, (245, 245, 220), (480, 40, 112, 47))
                pygame.draw.rect(window, (101, 78, 58), (475, 35, 122, 57), 5)
                title1 = self.title_font.render("Turn:", True, (0, 0, 0))
                window.blit(title1, (490, 53))

                if self.hints:
                    # Draws hint button
                    self.hint_rect = pygame.draw.rect(window, (245, 245, 220), (615, 40, 90, 47))
                    pygame.draw.rect(window, (101, 78, 58), (610, 35, 100, 57), 5)
                    button_text = self.writing_font.render("Hint", True, (0, 0, 0))
                    window.blit(button_text, (642, 70))
                    pic = pygame.transform.scale(pygame.image.load("Pieces/eye.png"), (30, 30))
                    window.blit(pic, (642, 41))

                # Starts game
                self.game_started = True
                return "start"
            elif self.tick_box.collidepoint(pos):
                # Decides whether hints are enabled or not
                if self.hints:
                    self.hints = False
                    self.tick_box = pygame.draw.rect(window, (245, 245, 220), (592, 83, 11, 11))
                else:
                    self.hints = True
                    words1a = self.writing_font.render("X", True, (0, 0, 0))
                    window.blit(words1a, (592, 82))
        return ""

    def draw_turn(self, window, colour):
        # Displays who's turn it is
        if colour:
            pic = pygame.transform.scale(pygame.image.load("Pieces/WK.png"), (35, 35))
            window.blit(pic, (547, 44))
        else:
            pic = pygame.transform.scale(pygame.image.load("Pieces/BK.png"), (35, 35))
            window.blit(pic, (547, 44))

    def end_game(self, window, colour):
        # Displays who won
        pygame.draw.rect(window, (245, 245, 220), (480, 110, 140, 42))
        pygame.draw.rect(window, (101, 78, 58), (475, 105, 150, 52), 5)
        if colour:
            end_title = self.title_font.render("White wins!", True, (0, 0, 0))
            window.blit(end_title, (485, 120))
        else:
            end_title = self.title_font.render("Black wins!", True, (0, 0, 0))
            window.blit(end_title, (485, 120))
