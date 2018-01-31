#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, os, math


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
        self.frame_count = fc
        self.frame_timer = 100
        self.vx = vx
        self.vy = vy

    def update(self, delta):
        self.frame_timer -= delta
        if self.frame_timer <= 0:
            self.frame_timer += 100
            self.frame_ind = (self.frame_ind + 1) % self.frame_count
        self.x += self.vx*(delta/1000)
        self.y += self.vy*(delta/1000)

    def draw(self, surface):
        offset_x = self.t_x + self.frame_ind*self.w
        surface.blit(self.__image, 
                     (self.x, self.y), 
                     pygame.Rect(offset_x, self.t_y, self.w, self.h))

    # Check_collision function checking is there intersection between this sprite and sprite2
    def check_collision(self, sprite2):
        # get this sprite center
        x1 = self.x + self.w/2 
        y1 = self.y + self.h/2
        # get second sprite center
        x2 = sprite2.x + sprite2.w/2
        y2 = sprite2.y + sprite2.h/2
        # check if there are bounding rectangles intersection
        return (abs(x1-x2) < (self.w+sprite2.w)/2) and (abs(y1-y2) < (self.h+sprite2.h)/2)
        