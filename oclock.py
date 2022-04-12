#!/usr/bin/env python

# On-line clock

import pygame, os, sys, time

class tc:
    def __init__(s):
        pygame.init()
        s.res = 174, 106
        s.screen = pygame.display.set_mode(s.res)
        s.out = pygame.Surface(s.res)
        pygame.display.set_caption("On-Line")
        s.clock = pygame.time.Clock()
        s.font = pygame.font.Font("OCRA.otf", 80)
        s.online = False
        s.total = 0
        if len(sys.argv) > 1:
            s.total = 60 * int(sys.argv[1])
        s.last = 0

    def events(s):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                s.running = False
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_o):
                s.online = not s.online
                s.last = time.time()
                # round up time to nearest minute when stopping:
                if s.online == False:
                    s.total = 60 * (s.total // 60 + 1)
                else:
                    # from https://freesound.org/people/wtermini/sounds/546450/
                    os.system("/usr/bin/play -q modem.flac &")
            # reset:
            if (s.online == False and event.type == pygame.KEYDOWN and event.key == pygame.K_r):
                s.total = 0
            # add one minute:
            if (s.online == False and event.type == pygame.KEYDOWN and event.key == pygame.K_a):
                s.total += 60

    def run(s):
        s.running = True
        while s.running:
            s.clock.tick(10)
            s.events()
            s.update()
        pygame.quit()

    def update(s):
        if s.online:
            tt = time.time()
            s.total += tt - s.last
            s.last = tt
            s.screen.fill((0, 0, 0))
            col = 0, 255, 0
        else:
            s.screen.fill((140, 140, 140))
            col = 0, 0, 0
        t = "%03u" % (s.total // 60)
        tr = s.font.render(t, True, col)
        #print(tr.get_size())
        s.screen.blit(tr, (0, 0))
        pygame.display.flip()

c = tc()
c.run()

