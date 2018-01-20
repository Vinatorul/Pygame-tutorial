#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, os


class Sprite:
    # загружаем с диска изображение
    __image = pygame.image.load(os.path.join(os.path.dirname(__file__),os.path.normpath("../Assets/sprites.png")))

    # сохраняем всю необходимую информацию
    def __init__(self, x, y, t_x, t_y, w, h):
        # положение спрайта в окне
        self.x = x
        self.y = y
        # отступ в текстуре
        self.t_x = t_x
        self.t_y = t_y
        # размер спрайта
        self.w = w
        self.h = h
        # фреймы анимации
        self.frame_ind = 0
        self.frame_count = 2
        # таймер на 100 милисекунд
        self.frame_timer = 100

    # функция update, производит обновление состояния объекта в зависимости от прошедшего времени
    def update(self, delta):
        # вычитаем из таймера прошедшее время
        self.frame_timer -= delta
        if self.frame_timer < 0:
            # если пришло время менять фреймы - меняю
            self.frame_timer = 100
            self.frame_ind = (self.frame_ind + 1) % self.frame_count

    # функция draw производит отрисовку спрайта на surface
    def draw(self, surface):
        # вычисляем отступ в текстуре, основываясь на исходном отступе и номере текущего фрейма анимации
        offset_x = self.t_x+self.frame_ind*self.w
        # рисуем в точке (x, y) кусочек текстуры, ограниченный прямоугольником (offset_x, t_y, w, h)
        surface.blit(self.__image, 
                     (self.x, self.y), 
                     pygame.Rect(offset_x, self.t_y, self.w, self.h)) 