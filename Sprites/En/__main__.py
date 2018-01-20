#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
# import sprite module
import sprite

WIDTH = 800
HEIGHT = 600
# Background color
BG_COLOR = "#CCCCCC"
# Text color
FG_COLOR = (40, 40, 40)
# Actor sizes
ACTOR_W = 44
ACTOR_H = 50
# actor image texture X offset
ACTOR_X_OFFSET = 936

def main():
    pygame.init()
    my_font = pygame.font.SysFont("Courier", 16)

    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)
    pygame.display.set_caption("Dinosaur game")
    clock = pygame.time.Clock()

    # actor sprite
    # 100,100 - screen position
    # ACTOR_X_OFFSET, 0 - x and у actor image offsets in texture
    # ACTOR_W, ACTOR_H - sprite width and height
    actor = sprite.Sprite(100, 100, ACTOR_X_OFFSET, 0, ACTOR_W, ACTOR_H)

    quit_game = False
    while not quit_game:
        # delta - last tick call milliseconds past
        delta = clock.tick(60)
        event = pygame.event.poll()
        while event.type != pygame.NOEVENT:
            if event.type == pygame.QUIT:
                quit_game = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                elif event.key == pygame.K_SPACE:
                    pygame.event.set_grab(not pygame.event.get_grab())
            event = pygame.event.poll()

        # update actor position
        actor.update(delta)

        # fill screen with BG_COLOR
        screen.fill(pygame.Color(BG_COLOR))
        # Draw actor sprite
        actor.draw(screen)
        fps_text = my_font.render("FPS = {0:.2f}"
                  .format(clock.get_fps()), True, FG_COLOR)
        screen.blit(fps_text, (10, 10))
        quit_text = my_font.render("Press Q to quit", True, FG_COLOR)        
        screen.blit(quit_text, (10, 30))
        pygame.display.flip()

    pygame.quit()

main()
