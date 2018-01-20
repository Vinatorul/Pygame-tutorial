#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
# подключаем модули sprite и random
import sprite

WIDTH = 800
HEIGHT = 600
# Цвет фона
BG_COLOR = "#CCCCCC"
# Цвет текста
FG_COLOR = (40, 40, 40)
# Размер игрока
ACTOR_W = 44
ACTOR_H = 50
# X оффсет спрайта игрока в текстуре
ACTOR_X_OFFSET = 936

def main():
    pygame.init()
    my_font = pygame.font.SysFont("Courier", 16)

    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF)
    pygame.display.set_caption("Dinosaur game")
    clock = pygame.time.Clock()

    # спрайт игрока
    # 100,100 - позиция на экране
    # ACTOR_X_OFFSET, 0 - отступы внутри текстуры по x и у соответственно
    # ACTOR_W, ACTOR_H - ширина и высота спрайта
    actor = sprite.Sprite(100, 100, ACTOR_X_OFFSET, 0, ACTOR_W, ACTOR_H)

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
        # Выводим спрайт игрока на экран
        actor.draw(screen)
        fps_text = my_font.render("FPS = {0:.2f}"
                  .format(clock.get_fps()), True, FG_COLOR)
        screen.blit(fps_text, (10, 10))
        quit_text = my_font.render("Нажмите Q для выхода", True, FG_COLOR)        
        screen.blit(quit_text, (10, 30))
        pygame.display.flip()

    pygame.quit()

main()
