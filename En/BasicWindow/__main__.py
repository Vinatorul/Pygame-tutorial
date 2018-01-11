import pygame

# desired window size
WIDTH = 800
HEIGHT = 600

def main():
    # pygame initialization
    pygame.init()
    # create window WIDTHxHEIGHT size with double buffering
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)

    quit_game = False
    # application lifeсycle 
    while not quit_game:
        # poll first event from queue
        event = pygame.event.poll()
        # process events while queue is not empty
        while event.type != pygame.NOEVENT:
            if event.type == pygame.QUIT:
                quit_game = True
            # poll next event from queue
            event = pygame.event.poll()

        # clear screen (fill with black)
        screen.fill(pygame.Color('black'))
        # -------------------
        # draw your stuff here
        # -------------------
        # swap buffers
        pygame.display.flip()

    # pygame finalization
    pygame.quit()

main()
