#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, sprite
import random, math

WIDTH = 800
HEIGHT = 600
BG_COLOR = "#F7F7F7"
FG_COLOR = (40, 40, 40)
ACTOR_W = 44
ACTOR_H = 50
ACTOR_X_OFFSET = 936
TILE_SIZE = 16
TILES_X_OFFSET = 16
TILES_Y_OFFSET = 52
GAME_VELOCITY = 300 
TILES_Y = HEIGHT-100
ACTOR_Y0 = TILES_Y + TILE_SIZE - ACTOR_H
# Добавляем константы для кактуса: отступ, ширина, высота и начальное положение
CACTUS_X_OFFSET = 244
CACTUS_W = 18
CACTUS_H = 35
# положение кактусов вычисляем относительно положения тайлов
CACTUS_Y0 = TILES_Y + TILE_SIZE - CACTUS_H
# Таймер создания кактусов (100 милисекунд)
CACTUS_CREATE_TIMER = 100

def main():
    pygame.init()
    my_font = pygame.font.SysFont("Courier", 16)

    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)
    pygame.display.set_caption("Dinosaur game")
    clock = pygame.time.Clock()

    actor = sprite.Sprite(100, ACTOR_Y0, ACTOR_X_OFFSET, 0, 
                          ACTOR_W, ACTOR_H, fc=2)

    tiles_count = WIDTH//TILE_SIZE + 1;
    tiles = []
    for i in range(-1, tiles_count-1):
        r = random.randrange(30)
        tile = sprite.Sprite(i*TILE_SIZE, TILES_Y, TILES_X_OFFSET + r*TILE_SIZE, 
                             TILES_Y_OFFSET, TILE_SIZE, TILE_SIZE, vx=-GAME_VELOCITY)
        tiles.append(tile)
    # список для хранения кактусов
    cactuses = []
    cactus_timer = 0

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
                elif event.key == pygame.K_ESCAPE:
                    pygame.event.set_grab(not pygame.event.get_grab())
                elif event.key == pygame.K_SPACE:
                    if actor.vy == 0:
                        actor.vy = -500
            event = pygame.event.poll()
        # ------------ Обновление игры -----------
        actor.update(delta)
        if actor.y < ACTOR_Y0 - 100:
            actor.vy = -actor.vy
        if actor.y >= ACTOR_Y0:
            actor.vy = 0
            actor.y = ACTOR_Y0
        for tile in tiles:
            tile.update(delta)
            if tile.x < -TILE_SIZE:
               tile.x += tiles_count*TILE_SIZE

        # Проверяем, не пришло ли время сгенерировать препятствие
        cactus_timer -= delta
        if cactus_timer <= 0:
            cactus_timer += CACTUS_CREATE_TIMER
            # получаем случайное число, для рандомизации генерации кактусов
            # вероятность создания препятствия равна 1/5
            r = random.randrange(5)
            if r == 0:
                # Если препятствие создалось - устанавливаем таймер в значение 1 секунда
                # Чтобы избежать слишком частого создания
                cactus_timer = 1000
                # Создаём кактус в позиции (WIDTH+1, CACTUS_Y0) - на том же уровне, что и игрок
                # за правой границей экрана
                # Не забываем про параметры изображения (отступ по х и у, ширину и высоту)
                # Обязательно задаём сокрость vx такую же, как у тайлов
                cactus = sprite.Sprite(WIDTH, CACTUS_Y0, CACTUS_X_OFFSET, 0, CACTUS_W, CACTUS_H, vx=-GAME_VELOCITY)
                cactuses.append(cactus)
        # Пробегаем по списку кактусов и обновляем положения
        for cactus in cactuses:
            cactus.update(delta)
            # если кактус оказался за левой границей экрана - удаляем его из списка
            if cactus.x < -CACTUS_W:
               cactuses.remove(cactus)
        # Проверяем, не пересекается ли персонаж с каким-то из кактусов
        for cactus in cactuses:
            # Если пересекается - отправляем себе событие о закрытии программы
            if actor.check_collision(cactus):
               print("LOL U DIED")
               pygame.event.post(pygame.event.Event(pygame.QUIT))
        # ------------ Отрисовка игрового мира ------------
        screen.fill(pygame.Color(BG_COLOR))
        for tile in tiles:
            tile.draw(screen)
        actor.draw(screen)
        # Кактусы рисуем после персонажа, чтобы он не зарывал их своей обводкой
        for cactus in cactuses:
           cactus.draw(screen)
        fps_text = my_font.render("FPS = {0:.2f}"
                  .format(clock.get_fps()), True, FG_COLOR)
        screen.blit(fps_text, (10, 10))
        quit_text = my_font.render("Нажмите Q для выхода", True, FG_COLOR)        
        screen.blit(quit_text, (10, 30))
        pygame.display.flip()

    pygame.quit()

main()
