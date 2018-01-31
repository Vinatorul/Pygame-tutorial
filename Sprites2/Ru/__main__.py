#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sprite
# подключаем модуль random и math
import random, math

WIDTH = 800
HEIGHT = 600
# Исправлен цвет
BG_COLOR = "#F7F7F7"
FG_COLOR = (40, 40, 40)
ACTOR_W = 44
ACTOR_H = 50
ACTOR_X_OFFSET = 936
# размер тайла
TILE_SIZE = 16
# отступ в текстуре
TILES_X_OFFSET = 16
TILES_Y_OFFSET = 52
# скорость игры (пиксели/секунда)
GAME_VELOCITY = 300
# Положение тайлов
TILES_Y = HEIGHT-100
# Положение игрока вычисляем на основе положения тайлов
ACTOR_Y0 = TILES_Y+TILE_SIZE - ACTOR_H

def main():
    pygame.init()
    my_font = pygame.font.SysFont("Courier", 16)

    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)
    pygame.display.set_caption("Dinosaur game")
    clock = pygame.time.Clock()

    # ACTOR_Y0 - положение динозавтра вычисляем на основе положения тайла
    # выставляем frame_count в значение 2
    actor = sprite.Sprite(100, ACTOR_Y0, ACTOR_X_OFFSET, 0, 
                          ACTOR_W, ACTOR_H, fc=2)

    # вычисляем необходимое количество тайлов
    # количество должно быть равно количеству тайлов, влезающих на экран
    # плюс один тайл, чтобы при любом смещении на экране не было пустот
    tiles_count = math.ceil(WIDTH/TILE_SIZE) + 1;
    # создаём пустой список
    tiles = []
    # и заполняем его тайлами
    for i in range(-1, tiles_count-1):
        # случайное число используем для выбора тайла из тайлсета
        r = random.randrange(30)
        # создаём тайл в точке (i*TILE_SIZE, TILES_Y) со скоростью -GAME_VELOCITY
        # знак минус нужен для того, чтобы тайлы двигались влево
        tile = sprite.Sprite(i*TILE_SIZE, TILES_Y, TILES_X_OFFSET + r*TILE_SIZE, 
                             TILES_Y_OFFSET, TILE_SIZE, TILE_SIZE, vx=-GAME_VELOCITY, vy=0)
        # добавляем в список
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
                # захват управление теперь производим по кнопке ESC
                elif event.key == pygame.K_ESCAPE:
                    pygame.event.set_grab(not pygame.event.get_grab())
                # на кнопку пробел теперь производится прыжок
                elif event.key == pygame.K_SPACE:
                    if actor.vy == 0:
                        actor.vy = -500
            event = pygame.event.poll()
        # ------------ Обновление игры -----------
        actor.update(delta)
        # Если персонаж поднялся выше, чем на 100 пикселей
        # то обращаем знак его скорости по у
        if actor.y < ACTOR_Y0 - 100:
            actor.vy = -actor.vy
        # Если положение персонажа ниже исходного, то обнуляем скорость
        # И выставляем в исходное положение
        if actor.y >= ACTOR_Y0:
            actor.vy = 0
            actor.y = ACTOR_Y0
        # Обновляем положение тайлов, если тайл полностью зашел за левую границу экрана,
        # то перемещаем его в конец списка
        for tile in tiles:
            tile.update(delta)
            if tile.x < -TILE_SIZE:
               tile.x += tiles_count*TILE_SIZE

        # ------------ Отрисовка игрового мира ------------
        screen.fill(pygame.Color(BG_COLOR))
        # рисуем тайлы
        for tile in tiles:
            tile.draw(screen)
        # динозавтра рисуем обязательно после тайлов, чтобы он закрывал их своей обводкой
        actor.draw(screen)
        fps_text = my_font.render("FPS = {0:.2f}"
                  .format(clock.get_fps()), True, FG_COLOR)
        screen.blit(fps_text, (10, 10))
        quit_text = my_font.render("Нажмите Q для выхода", True, FG_COLOR)        
        screen.blit(quit_text, (10, 30))
        pygame.display.flip()

    pygame.quit()

main()
