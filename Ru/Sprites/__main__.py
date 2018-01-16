#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
# подключаем модули sprite и random
import sprite
import random

WIDTH = 800
HEIGHT = 600
# Цвет фона
BG_COLOR = "#CCCCCC"
# Цвет текста
FG_COLOR = (40, 40, 40)
# Размер тайла
TILE_SIZE = 16
# Размер игрока
ACTOR_W = 44
ACTOR_H = 50
# Размер маленького кактуса
CACTUS_H = 37
CACTUS_W = 18
# X оффсет спрайта игрока в текстуре
ACTOR_X_OFFSET = 936
# Y оффсет тайлов земли в текстуре
TILE_Y_OFFSET = 52
# X оффсет спрайта кактуса в текстуре
CACTUS_X_OFFSET = 227

def main():
    pygame.init()
    my_font = pygame.font.SysFont("Courier", 16)

    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)
    pygame.display.set_caption("Dinosaur game")
    clock = pygame.time.Clock()

    # создаём список тайлов земли
    floor = []
    for i in range(WIDTH//16):
        # получаю случайный тайл
        rd = random.randrange(1, 40)
        floor.append(sprite.Sprite(i*TILE_SIZE, HEIGHT-100, rd*16, TILE_Y_OFFSET, TILE_SIZE, TILE_SIZE, 1))
    # спрайт игрока
    actor = sprite.Sprite(100, HEIGHT-100-(ACTOR_H-TILE_SIZE), ACTOR_X_OFFSET, 0, ACTOR_W, ACTOR_H, 2)
    # спрайт кактуса
    cactus = sprite.Sprite(500, HEIGHT-100-(CACTUS_H-TILE_SIZE), CACTUS_X_OFFSET, 0, CACTUS_W, CACTUS_H, 1)

    quit_game = False
    while not quit_game:
        # delta - количество милисекунд, прошедших с прошлого фрейма
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

        # Обновляем состояние игрока
        actor.update(delta)

        # Теперь фон и текст рисуем цветом, заданным в константах
        screen.fill(pygame.Color(BG_COLOR))
        # Выводим тайлы земли на экран
        for sp in floor:
            sp.draw(screen)
        # Выводим спрайт игрока на экран
        actor.draw(screen)
        # Выводим спрайт кактуса на экран
        cactus.draw(screen)
        fps_text = my_font.render("FPS = {0:.2f}"
                  .format(clock.get_fps()), True, FG_COLOR)
        screen.blit(fps_text, (10, 10))
        quit_text = my_font.render("Нажмите Q для выхода", True, FG_COLOR)        
        screen.blit(quit_text, (10, 30))
        pygame.display.flip()

    pygame.quit()

main()
