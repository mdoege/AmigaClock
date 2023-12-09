#!/usr/bin/env python3

# 1-D Perlin noise-based animation

import pygame
from random import random, randint
import time

SCALEX, SCALEY = 123, 127
RADIUS = 50

def inter(a, b, w):
    "Interpolate between a and b using weight w"
    return (b - a) * ((w * (w * 6 - 15) + 10) * w * w * w) + a  # smootherstep

def get_noise(SCALE, start = None):
    "Get 1-D Perlin noise"
    stop = 2 * random() - 1
    if start == None:
        start = 2 * random() - 1
    #print(start, stop)
    arr = []
    for tt in range(SCALE):
        t = tt / SCALE
        y1 = t * start
        y2 = (t - 1) * stop
        arr.append(inter(y1, y2, t))
    return arr, stop

class Perlin:
    def __init__(s):
        pygame.init()
        s.res = 1200, 900  # default window size
        s.screen = pygame.display.set_mode(s.res, pygame.RESIZABLE)
        pygame.display.set_caption('Worm')
        s.clock = pygame.time.Clock()
        s.noise1, s.last1 = get_noise(SCALEX)
        s.noise2, s.last2 = get_noise(SCALEY)
        s.x, s.y = 0, 0
        s.color = 51*randint(0, 5), 51*randint(0, 5), 51*randint(0, 5)

    def events(s):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: s.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                pygame.image.save(s.screen,
                        time.strftime("worm-%y%m%d_%H%M%S.png"))
            if event.type == pygame.VIDEORESIZE:
                s.res = event.w, event.h
                #print(s.res)
                s.screen = pygame.display.set_mode(s.res, pygame.RESIZABLE)

    def run(s):
        s.running = True
        while s.running:
            s.clock.tick(30)
            s.events()
            s.update()
        pygame.quit()

    def update(s):
        dx = int(s.res[0] * s.noise1.pop(0))
        dy = int(s.res[1] * s.noise2.pop(0))
        s.x += dx / 20
        s.y += dy / 20
        s.x = max(-s.res[0]//2, min(s.res[0]//2, s.x))
        s.y = max(-s.res[1]//2, min(s.res[1]//2, s.y))
        if len(s.noise1) == 0:
            s.noise1, s.last1 = get_noise(SCALEX, start = s.last1)
        if len(s.noise2) == 0:
            s.noise2, s.last2 = get_noise(SCALEY, start = s.last2)
        if random() < .2:
            s.color = 51*randint(0, 5), 51*randint(0, 5), 51*randint(0, 5)
        pygame.draw.circle(s.screen, s.color,
            (s.x + s.res[0]//2, s.y + s.res[1]//2), RADIUS)
        
        pygame.display.flip()

c = Perlin()
c.run()

