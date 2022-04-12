#!/usr/bin/env python

# Text clock

import pygame, time

class tc:
    def __init__(s):
        pygame.init()
        s.res = 640, 145
        s.screen = pygame.display.set_mode(s.res)
        s.out = pygame.Surface(s.res)
        pygame.display.set_caption("Text Clock")
        s.clock = pygame.time.Clock()
        s.font = pygame.font.Font("OCRA.otf", 110)

    def events(s):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or 
               (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                s.running = False

    def run(s):
        s.running = True
        while s.running:
            s.clock.tick(10)
            s.events()
            s.update()
        pygame.quit()

    def update(s):
        s.screen.fill((0, 0, 0))

        t = time.strftime('%H:%M:%S', time.localtime())
        tr = s.font.render(t, True, (0, 255, 0))
        #print(tr.get_size())
        s.screen.blit(tr, (0, 0))
        pygame.display.flip()

c = tc()
c.run()

