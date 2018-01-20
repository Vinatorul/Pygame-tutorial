import pygame

WIDTH = 800
HEIGHT = 600

def main():
    pygame.init()
    # import Courier font
    my_font = pygame.font.SysFont("Courier", 16)

    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)
    # Set window caption
    pygame.display.set_caption("Hello, pygame")
    # Pygame clock initialization
    clock = pygame.time.Clock()

    quit_game = False
    while not quit_game:
        # Set FPS cap
        clock.tick(60)
        event = pygame.event.poll()
        while event.type != pygame.NOEVENT:
            if event.type == pygame.QUIT:
                quit_game = True
            # keydown event processing
            elif event.type == pygame.KEYDOWN:
                # if q key pressed
                if event.key == pygame.K_q:
                    # add QUIT event to queue
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                # if Space pressed
                elif event.key == pygame.K_SPACE:
                    # toggle grab mode
                    pygame.event.set_grab(not pygame.event.get_grab())
            event = pygame.event.poll()

        screen.fill(pygame.Color('black'))
        # render text to fps_text variable
        # (255, 255, 255) - color in (R, G, B) format
        fps_text = my_font.render("FPS = {0:.2f}"
                  .format(clock.get_fps()), True, (255, 255, 255))
        # draw fps_text at (10, 10)
        screen.blit(fps_text, (10, 10))
        # render tip to quit_text variable
        quit_text = my_font.render("Press Q to quit", True, (255, 255, 255))        
        # draw quit_text at (10, 30)
        screen.blit(quit_text, (10, 30))
        # check if grab mode is active
        if pygame.event.get_grab():
            grab_text = my_font.render("Press SPACE to exit input grab mode", True, (255, 255, 255))       
        else:
            grab_text = my_font.render("Press SPACE to enter input grab mode", True, (255, 255, 255))
        # draw text near the middle of the screen
        screen.blit(grab_text, (WIDTH/2 - 170, HEIGHT/2 - 15))

        pygame.display.flip()

    pygame.quit()

main()
