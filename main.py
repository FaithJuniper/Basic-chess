import pygame

WIN = pygame.display.set_mode((760, 440))
pygame.display.set_caption('Chess')


if __name__ == '__main__':
    run = True
    clock = pygame.time.Clock()
    WIN.fill((53, 101, 77))
    pygame.draw.rect(WIN, (42, 81, 62), (0, 0, 760, 440), 10)
    pygame.draw.rect(WIN, (27,52, 40), (0, 0, 760, 440), 3)
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()
