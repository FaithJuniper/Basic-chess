import pygame
import board
import menu

WIN = pygame.display.set_mode((760, 480))
pygame.display.set_caption('Chess')


if __name__ == '__main__':
    run = True
    clock = pygame.time.Clock()
    WIN.fill((53, 101, 77))
    for y in range(480):
        if y%10 == 0:
            for x in range(760):
                if x%10 == 0:
                    pygame.draw.rect(WIN, (48, 91, 71), (x, y, 5, 5))
    pygame.draw.rect(WIN, (42, 81, 62), (0, 0, 760, 480), 10)
    pygame.draw.rect(WIN, (27,52, 40), (0, 0, 760, 480), 3)
    board = board.board()
    board.draw_squares(WIN)
    board.draw_pieces(WIN)
    menu = menu.menu()
    menu.draw_boxes(WIN)
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()
