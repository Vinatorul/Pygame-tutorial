#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sprite
# import random and math
import random, math

WIDTH = 800
HEIGHT = 600
# Fix BG color
BG_COLOR = "#F7F7F7"
FG_COLOR = (40, 40, 40)
ACTOR_W = 44
ACTOR_H = 50
ACTOR_X_OFFSET = 936
# tile size
TILE_SIZE = 16
# tiles offset in tilemap 
TILES_X_OFFSET = 16
TILES_Y_OFFSET = 52
# game velocity (pixels pre second)
GAME_VELOCITY = 300
# tiles screen position
TILES_Y = HEIGHT-100
# Calculate actor pos depending on tiles position
ACTOR_Y0 = TILES_Y+TILE_SIZE - ACTOR_H

def main():
    pygame.init()
    my_font = pygame.font.SysFont("Courier", 16)

    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)
    pygame.display.set_caption("Dinosaur game")
    clock = pygame.time.Clock()

    # ACTOR_Y0 - dinosaur pos calculated based on tiles pos
    # set frame_count to 2
    actor = sprite.Sprite(100, ACTOR_Y0, ACTOR_X_OFFSET, 0, 
                          ACTOR_W, ACTOR_H, fc=2)

    # caculate required number of tiles
    # it should be equal to number of tiles, that fit into the screen
    # plus one tile, so there will be no sprite flickering at screen edges
    tiles_count = math.ceil(WIDTH/TILE_SIZE) + 1;
    # create empty list
    tiles = []
    # and fill it with tils
    for i in range(-1, tiles_count-1):
        # generate random number to choose random tile from tileset
        r = random.randrange(30)
        # create tile at (i*TILE_SIZE, TILES_Y) with -GAME_VELOCITY speed
        tile = sprite.Sprite(i*TILE_SIZE, TILES_Y, TILES_X_OFFSET + r*TILE_SIZE, 
                             TILES_Y_OFFSET, TILE_SIZE, TILE_SIZE, vx=-GAME_VELOCITY, vy=0)
        # add it to list
        tiles.append(tile)

    quit_game = False
    while not quit_game:
        delta = clock.tick(60)
        event = pygame.event.poll()
        while event.type != pygame.NOEVENT:
            if event.type == pygame.QUIT:
                quit_game = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                # grab mode is now toggled pressing ESC
                elif event.key == pygame.K_ESCAPE:
                    pygame.event.set_grab(not pygame.event.get_grab())
                # start actor jump on SPACE key pressed
                elif event.key == pygame.K_SPACE:
                    if actor.vy == 0:
                        actor.vy = -500
            event = pygame.event.poll()
        # ------------ Game state update -----------
        actor.update(delta)
        # If actor rose higher than 100 px
        # reverse it's y velocity sign
        if actor.y < ACTOR_Y0 - 100:
            actor.vy = -actor.vy
        # If actor fell below ACTOR_Y0 height
        # set it's y coordinate to ACTOR_Y0 and set y velocity to zero 
        if actor.y >= ACTOR_Y0:
            actor.vy = 0
            actor.y = ACTOR_Y0
        # Update tiles position. Move tile to the end of tiles line if it's
        # position is to the left of screen border
        for tile in tiles:
            tile.vx -= delta/1000
            tile.update(delta)
            if tile.x < -TILE_SIZE:
               tile.x += tiles_count*TILE_SIZE

        # ------------ Game state draw ------------
        screen.fill(pygame.Color(BG_COLOR))
        # draw tiles
        for tile in tiles:
            tile.draw(screen)
        # draw dinosaur after tiles, so it's outline will higlight it
        actor.draw(screen)
        fps_text = my_font.render("FPS = {0:.2f}"
                  .format(clock.get_fps()), True, FG_COLOR)
        screen.blit(fps_text, (10, 10))
        quit_text = my_font.render("Press Q to Exit", True, FG_COLOR)        
        screen.blit(quit_text, (10, 30))
        pygame.display.flip()

    pygame.quit()

main()
