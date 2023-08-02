import pygame
import board
import gui

WIN = pygame.display.set_mode((743, 480))
pygame.display.set_caption('Chess')
GAME = False


if __name__ == '__main__':
    run = True
    clock = pygame.time.Clock()
    gui = gui.gui()
    gui.draw_menu(WIN)
    board = board.board()
    board.draw_squares(WIN)
    board.draw_pieces(WIN)
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                action = gui.click(WIN)
                if action == "start":
                    GAME = True
                elif action == "hint":
                    board.find_hint()
                action = board.click(WIN)
                if action == "W":
                    gui.end_game(WIN, True)
                elif action == "B":
                    gui.end_game(WIN, False)
        if GAME:
            board.game_started = True
            gui.draw_turn(WIN, board.turn)
            board.draw(WIN)
        pygame.display.update()
    pygame.quit()
