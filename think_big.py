#!/usr/bin/env python

# Thinking Machines-like LEDs

import pygame
import numpy
import random, time

RESX, RESY = 16, 32     # LED resolution
SIZE = 9                # LED size
COLOR = 200, 0, 0       # LED RGB color
UPDATE = 2/16           # update interval

led = numpy.zeros((RESX, RESY))

class Dazzler:
    def __init__(s):
        pygame.init()
        # total vertical size: 3 full panels and 10 rows from a 4th panel
        #   (https://housedillon.com/blog/resurrected-led-panels/)
        s.screen = pygame.display.set_mode((RESX * SIZE, (3*32+10) * SIZE))
        pygame.display.set_caption('Think')
        s.clock = pygame.time.Clock()
        s.dazz = pygame.Surface((RESX, RESY))
        s.last = 0

    def events(s):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: s.running = False

    def run(s):
        s.running = True
        while s.running:
            s.clock.tick(50)
            s.events()
            s.update()
        pygame.quit()

    def update(s):
        if time.time() - s.last > UPDATE:
            s.last = time.time()

            for j in range(RESY):
                if (j // 4) % 2:
                    led[1:,j] = led[:-1,j]
                    led[0,j] = random.choice([0, 0, 0, 1])
                else:
                    led[:-1,j] = led[1:,j]
                    led[-1,j] = random.choice([0, 0, 0, 1])

                for i in range(RESX):
                    if led[i,j]:
                        pygame.draw.line(s.dazz, COLOR, (i, j), (i, j), 1)
                    else:
                        pygame.draw.line(s.dazz, (0, 0, 0), (i, j), (i, j), 1)

        out = pygame.transform.scale(s.dazz, (RESX * SIZE, RESY * SIZE))

        # pattern is the same on all 7 panels
        for b in range(7):
            s.screen.blit(out, (0, b * RESY * SIZE))
        
        pygame.display.flip()

c = Dazzler()
c.run()

