import pygame

WIDTH = 800
HEIGHT = 600

def main():
    pygame.init()

    my_font = pygame.font.SysFont("Courier", 16)

    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)
    pygame.display.set_caption("Hello, pygame")

    pygame.event.set_blocked(pygame.MOUSEMOTION)
    clock = pygame.time.Clock()

    quit_game = False
    while not quit_game:
        clock.tick(60)
        event = pygame.event.poll()
        while event.type != pygame.NOEVENT:
            if event.type == pygame.QUIT:
                quit_game = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                elif event.key == pygame.K_ESCAPE:
                    pygame.event.set_grab(not pygame.event.get_grab())
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pygame.event.set_grab(True)
            event = pygame.event.poll()

        screen.fill(pygame.Color('black'))
        the_text = my_font.render("FPS = {0:.2f}"
                  .format(clock.get_fps()), True, (255, 255, 255))
        screen.blit(the_text, (10, 10))
        the_text = my_font.render("Press Q to quit", True, (255, 255, 255))
        screen.blit(the_text, (10, 30))
        if pygame.event.get_grab():
            the_text = my_font.render("Press ESC to exit input grab mode", True, (255, 255, 255))       
        else:
            the_text = my_font.render("Click or press ECS to enter input grab mode", True, (255, 255, 255))
        screen.blit(the_text, (WIDTH/2 - 170, HEIGHT/2 - 15))

        pygame.display.flip()

    pygame.quit()

main()
