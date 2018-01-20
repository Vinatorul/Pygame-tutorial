#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pygame, os


class Sprite:
    # load image
    __image = pygame.image.load(os.path.join(os.path.dirname(__file__),os.path.normpath("../Assets/sprites.png")))

    # collect all sprite imformation 
    def __init__(self, x, y, t_x, t_y, w, h):
        # sprite screen position
        self.x = x
        self.y = y
        # sprite offsets
        self.t_x = t_x
        self.t_y = t_y
        # sprite sizes
        self.w = w
        self.h = h
        # animation frams
        self.frame_ind = 0
        self.frame_count = 2
        # 100 milliseconds timer
        self.frame_timer = 100

    # update procedure updates the state of the object depending on the time past
    def update(self, delta):
        # subtract delta from timer
        self.frame_timer -= delta
        if self.frame_timer < 0:
            # if timer expired - reset and change frame
            self.frame_timer = 100
            self.frame_ind = (self.frame_ind + 1) % self.frame_count

    # draw - procedure that draws sprite on the surface
    def draw(self, surface):
        # calculate frame offset from base offset and current frame
        offset_x = self.t_x+self.frame_ind*self.w
        # draw at (x, y) point, bounded by (offset_x, t_y, w, h) rectangle
        surface.blit(self.__image, 
                     (self.x, self.y), 
                     pygame.Rect(offset_x, self.t_y, self.w, self.h)) 