import pygame
import board
import gui

WIN = pygame.display.set_mode((760, 480))
pygame.display.set_caption('Chess')


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
            elif event.type == pygame.KEYDOWN:
                gui.type(WIN, event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                gui.click(WIN)
        pygame.display.update()
    pygame.quit()
