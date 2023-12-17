#!/usr/bin/env python

# "Intergalactic supercomputers for all" (https://www.youtube.com/watch?v=7f8jgvvJe-Q)

import pygame
import numpy
import random, time

RES = 32                # LED resolution
COLOR = 200, 200, 0     # LED RGB color

RES2 = RES/2
SRES = 1024
tile = 1            # number of tiles (press T to change)
slow = False        # slow mode (press S to toggle)

# set random bulb frequencies
state = numpy.zeros((RES, RES))
for j in range(RES):
    for i in range(RES):
        state[j,i] = int(random.gauss(10000, 200))

is_on = numpy.zeros((RES, RES))
cur = numpy.zeros((RES, RES))
cur[:,:] = state[:,:]

def ttime():
    if slow:
        return .5 * time.time()
    else:
        return time.time()

class Dazzler:
    def __init__(s):
        pygame.init()
        s.res = SRES, int(0.75 * SRES)
        s.screen = pygame.display.set_mode(s.res, pygame.RESIZABLE)
        pygame.display.set_caption('Supercomputer')
        s.clock = pygame.time.Clock()
        s.dazz = pygame.Surface((RES, RES))
        s.last = 0
        s.paused = False
        s.step = False

    def events(s):
        global tile, slow

        for event in pygame.event.get():
            if event.type == pygame.QUIT: s.running = False
            if event.type == pygame.VIDEORESIZE:
                s.res = event.w, event.h
                #print(s.res)
                s.screen = pygame.display.set_mode(s.res, pygame.RESIZABLE)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                s.paused = not s.paused
            if event.type == pygame.KEYDOWN and event.key == pygame.K_PERIOD:
                s.step = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
                tile += 1
                if tile > 5:
                    tile = 1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                slow = not slow

    def run(s):
        s.running = True
        while s.running:
            if slow:
                s.clock.tick(8)
            else:
                s.clock.tick(100)
            s.events()
            s.update()
        pygame.quit()

    def update(s):
        if s.paused and not s.step:
            return
        #print(1/(time.time()-s.last))
        #s.last = time.time()

        s.step = False

        for j in range(RES):
            for i in range(RES):
                cur[j,i] -= 100
                if cur[j,i] < 0:
                    cur[j,i] = state[j,i] + cur[j,i]
                    is_on[j,i] = 1 - is_on[j,i]
                    if is_on[j,i]:
                        pygame.draw.line(s.dazz, COLOR, (i,j), (i,j))
                    else:
                        pygame.draw.line(s.dazz, (0, 0, 0), (i,j), (i,j))

        tres = s.res[0] // tile, s.res[1] // tile
        out = pygame.transform.scale(s.dazz, tres)
        for y in range(tile):
            for x in range(tile):
                s.screen.blit(out, (tres[0] * x, tres[1] * y))
        
        pygame.display.flip()

c = Dazzler()
c.run()

