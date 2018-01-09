import pygame

WIDTH = 800
HEIGHT = 600

def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)

    quit_game = False
    while not quit_game:
        event = pygame.event.poll()
        while event.type != pygame.NOEVENT:
            if event.type == pygame.QUIT:
                quit_game = True
            event = pygame.event.poll()

        screen.fill(pygame.Color('black'))
        pygame.display.flip()

    pygame.quit()

main()
