#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, os


class Sprite:
    __image = pygame.image.load(os.path.join(os.path.dirname(__file__),os.path.normpath("../Assets/sprites.png")))

    def __init__(self, x, y, t_x, t_y, w, h, vx=0, vy=0, fc=1):
        self.x = x
        self.y = y
        self.t_x = t_x
        self.t_y = t_y
        self.w = w
        self.h = h
        self.frame_ind = 0
        # инициализируем frame_count значением fc
        self.frame_count = fc
        self.frame_timer = 100
        # инициализиурем скорость по x и y
        self.vx = vx
        self.vy = vy

    def update(self, delta):
        self.frame_timer -= delta
        # исправлена ошибка из-за которой фреймы могли отображаться неравномерно
        if self.frame_timer <= 0:
            self.frame_timer += 100
            self.frame_ind = (self.frame_ind + 1) % self.frame_count
        # скорость измеряется в пиксели/секунды, поэтому просто домножаем на кол-во секунд 
        self.x += self.vx*(delta/1000)
        self.y += self.vy*(delta/1000)

    def draw(self, surface):
        offset_x = self.t_x + self.frame_ind*self.w
        surface.blit(self.__image, 
                     (self.x, self.y), 
                     pygame.Rect(offset_x, self.t_y, self.w, self.h))
