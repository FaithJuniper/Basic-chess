import pygame
import server


class gui:
    def __init__(self):
        pygame.font.init()

        # Current text values
        self.current_text = ""
        self.current_input = None
        self.chat_text = []

        # The base rectangles of buttons
        self.join_rect = None
        self.create_rect = None
        self.send_rect = None

        # Has the game started yet
        self.game_started = False

        # Font styles
        self.title_font = pygame.font.Font(None, 32)
        self.writing_font = pygame.font.Font(None, 22)
        self.arrow_font = pygame.font.Font(None, 30)

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

        # Adds 'buttons'
        self.join_rect = pygame.draw.rect(window, (186, 140, 99), (645, 345, 55, 30))
        pygame.draw.rect(window, (101, 78, 58), (642, 342, 61, 36), 3)
        button_text1 = self.writing_font.render("Join", True, (0, 0, 0))
        window.blit(button_text1, (655, 353))
        self.create_rect = pygame.draw.rect(window, (186, 140, 99), (495, 165, 75, 30))
        pygame.draw.rect(window, (101, 78, 58), (492, 162, 81, 36), 3)
        button_text2 = self.writing_font.render("Create", True, (0, 0, 0))
        window.blit(button_text2, (505, 173))

        # Adds text
        title1 = self.title_font.render("Create new game", True, (0, 0, 0))
        window.blit(title1, (490, 80))
        title2 = self.title_font.render("Join game", True, (0, 0, 0))
        window.blit(title2, (490, 260))
        words1a = self.writing_font.render("You'll be given a code, give", True, (0, 0, 0))
        words1b = self.writing_font.render("this to a friend so they can join.", True, (0, 0, 0))
        window.blit(words1a, (490, 112))
        window.blit(words1b, (490, 132))
        words2a = self.writing_font.render("Input the code below to join", True, (0, 0, 0))
        words2b = self.writing_font.render("your friend's game.", True, (0, 0, 0))
        window.blit(words2a, (490, 292))
        window.blit(words2b, (490, 312))

        # Adds 'textbox'
        text_input = self.writing_font.render(self.current_text, True, (0, 0, 0))
        self.current_input = text_input
        window.blit(text_input, (500, 353))

    def type(self, window, event):
        # Sets where the text will go
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
            self.current_input = self.writing_font.render(self.current_text, True, (0, 0, 0))
            window.blit(self.current_input, pos)
        else:
            # Adds a character in the 'textbox'
            self.current_text += event.unicode
            self.current_input = self.writing_font.render(self.current_text, True, (0, 0, 0))
            window.blit(self.current_input, pos)

    def click(self, window):
        pos = pygame.mouse.get_pos()

        if self.game_started:
            # Sends message
            if self.send_rect.collidepoint(pos):
                server.send_message(self.current_text)
                self.current_text = ""
        else:
            # Starts game
            if self.join_rect.collidepoint(pos):
                pygame.draw.rect(window, (53, 101, 77), (475, 65, 250, 340))
                for y in range(480):
                    if y % 10 == 0:
                        for x in range(760):
                            if x % 10 == 0 and ((475 < x < 725) and (65 < y < 405)):
                                pygame.draw.rect(window, (48, 91, 71), (x, y, 5, 5))
                address = self.current_text
                self.create(window)
                server.join(address, window, self.chat_text, self.writing_font)
            elif self.create_rect.collidepoint(pos):
                pygame.draw.rect(window, (53, 101, 77), (475, 65, 250, 340))
                for y in range(480):
                    if y % 10 == 0:
                        for x in range(760):
                            if x % 10 == 0 and ((475 < x < 725) and (65 < y < 405)):
                                pygame.draw.rect(window, (48, 91, 71), (x, y, 5, 5))
                self.create(window)
                server.new_server(window, self.chat_text, self.writing_font)

    def create(self, window):
        self.game_started = True

        # Draws chat box
        pygame.draw.rect(window, (245, 245, 220), (480, 40, 240, 200))
        pygame.draw.rect(window, (101, 78, 58), (475, 35, 250, 210), 5)
        pygame.draw.rect(window, (186, 140, 99), (480, 245, 200, 30))
        pygame.draw.rect(window, (101, 78, 58), (475, 240, 210, 40), 5)
        pygame.draw.rect(window, (186, 140, 99), (685, 245, 35, 30))
        self.send_rect = pygame.draw.rect(window, (101, 78, 58), (680, 240, 45, 40), 5)

        # Adds 'textbox'
        self.current_text = ""
        text_input = self.writing_font.render(self.current_text, True, (0, 0, 0))
        self.current_input = text_input
        window.blit(text_input, (485, 253))

        # Adds text
        arrow = self.arrow_font.render(">", True, (0, 0, 0))
        window.blit(arrow, (696, 248))
