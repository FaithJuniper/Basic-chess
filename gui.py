import pygame


class gui:
    def __init__(self):
        # Decides which 'textbox' the user can currently type in
        self.current_text = ""
        self.current_input = None

        # The base rectangles of buttons
        self.join_rect = None
        self.create_rect = None

        # Has the game started yet
        self.game_started = False

        pygame.font.init()

    def draw_menu(self, window):
        # Draws background
        window.fill((53, 101, 77))
        for y in range(480):
            if y % 10 == 0:
                for x in range(760):
                    if x % 10 == 0:
                        pygame.draw.rect(window, (48, 91, 71), (x, y, 5, 5))
        pygame.draw.rect(window, (42, 81, 62), (0, 0, 760, 480), 10)
        pygame.draw.rect(window, (27, 52, 40), (0, 0, 760, 480), 3)

        # Draws menu
        pygame.draw.rect(window, (245, 245, 220), (480, 70, 240, 150))
        pygame.draw.rect(window, (101, 78, 58), (475, 65, 250, 160), 5)
        pygame.draw.rect(window, (245, 245, 220), (480, 250, 240, 150))
        pygame.draw.rect(window, (101, 78, 58), (475, 245, 250, 160), 5)
        pygame.draw.rect(window, (186, 140, 99), (495, 345, 135, 30))
        pygame.draw.rect(window, (101, 78, 58), (492, 342, 141, 36), 3)

        # Font styles
        title_font = pygame.font.Font(None, 32)
        writing_font = pygame.font.Font(None, 22)

        # Adds 'buttons'
        self.join_rect = pygame.draw.rect(window, (186, 140, 99), (645, 345, 55, 30))
        pygame.draw.rect(window, (101, 78, 58), (642, 342, 61, 36), 3)
        button_text1 = writing_font.render("Join", True, (0, 0, 0))
        window.blit(button_text1, (655, 353))
        self.create_rect = pygame.draw.rect(window, (186, 140, 99), (495, 165, 75, 30))
        pygame.draw.rect(window, (101, 78, 58), (492, 162, 81, 36), 3)
        button_text2 = writing_font.render("Create", True, (0, 0, 0))
        window.blit(button_text2, (505, 173))

        # Adds text
        title1 = title_font.render("Create new game", True, (0, 0, 0))
        window.blit(title1, (490, 80))
        title2 = title_font.render("Join game", True, (0, 0, 0))
        window.blit(title2, (490, 260))
        words1a = writing_font.render("You'll be given a code, give", True, (0, 0, 0))
        words1b = writing_font.render("this to a friend so they can join.", True, (0, 0, 0))
        window.blit(words1a, (490, 112))
        window.blit(words1b, (490, 132))
        words2a = writing_font.render("Input the code below to join", True, (0, 0, 0))
        words2b = writing_font.render("your friend's game.", True, (0, 0, 0))
        window.blit(words2a, (490, 292))
        window.blit(words2b, (490, 312))

        # Adds 'textbox'
        text_input = writing_font.render(self.current_text, True, (0, 0, 0))
        self.current_input = text_input
        window.blit(text_input, (500, 353))

    def type(self, window, event):
        writing_font = pygame.font.Font(None, 22)
        if self.game_started:
            rect = (480, 245, 200, 30)
            pos = (485, 253)
        else:
            rect = (495, 345, 130, 30)
            pos = (500, 353)
        if event.key == pygame.K_BACKSPACE:
            # Deletes a character in the 'textbox'
            pygame.draw.rect(window, (186, 140, 99), rect)
            self.current_text = self.current_text[:-1]
            self.current_input = writing_font.render(self.current_text, True, (0, 0, 0))
            window.blit(self.current_input, pos)
        else:
            # Adds a character in the 'textbox'
            self.current_text += event.unicode
            self.current_input = writing_font.render(self.current_text, True, (0, 0, 0))
            window.blit(self.current_input, pos)

    def click(self, window):
        pos = pygame.mouse.get_pos()
        if not self.game_started:
            if self.join_rect.collidepoint(pos):
                pygame.draw.rect(window, (53, 101, 77), (475, 65, 250, 340))
                for y in range(480):
                    if y % 10 == 0:
                        for x in range(760):
                            if x % 10 == 0 and ((475 < x < 725) and (65 < y < 405)):
                                pygame.draw.rect(window, (48, 91, 71), (x, y, 5, 5))
                self.create(window)
            elif self.create_rect.collidepoint(pos):
                pygame.draw.rect(window, (53, 101, 77), (475, 65, 250, 340))
                for y in range(480):
                    if y % 10 == 0:
                        for x in range(760):
                            if x % 10 == 0 and ((475 < x < 725) and (65 < y < 405)):
                                pygame.draw.rect(window, (48, 91, 71), (x, y, 5, 5))
                self.create(window)

    def create(self, window):
        self.game_started = True

        # Draws chat box
        pygame.draw.rect(window, (245, 245, 220), (480, 40, 240, 200))
        pygame.draw.rect(window, (101, 78, 58), (475, 35, 250, 210), 5)
        pygame.draw.rect(window, (186, 140, 99), (480, 245, 200, 30))
        pygame.draw.rect(window, (101, 78, 58), (475, 240, 210, 40), 5)
        pygame.draw.rect(window, (186, 140, 99), (685, 245, 35, 30))
        pygame.draw.rect(window, (101, 78, 58), (680, 240, 45, 40), 5)

        # Font styles
        writing_font = pygame.font.Font(None, 22)
        arrow_font = pygame.font.Font(None, 30)

        # Adds 'textbox'
        self.current_text = ""
        text_input = writing_font.render(self.current_text, True, (0, 0, 0))
        self.current_input = text_input
        window.blit(text_input, (485, 253))

        # Adds text
        arrow = arrow_font.render(">", True, (0, 0, 0))
        window.blit(arrow, (696, 248))
