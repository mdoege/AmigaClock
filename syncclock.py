#!/usr/bin/env python

# Sync clock

import pygame, os, time

SYNCTIME = 30 * 60      # syncing interval in seconds

def do_sync():
    os.system("/home/martin/bin/ntpdate ntp1.t-online.de > /tmp/ntpsync.txt")
    os.system("/home/martin/bin/hwclock -w")

class sc:
    def __init__(s):
        pygame.init()
        s.res = 640, 185
        s.screen = pygame.display.set_mode(s.res)
        s.out = pygame.Surface(s.res)
        pygame.display.set_caption("Sync Clock")
        s.clock = pygame.time.Clock()
        s.font = pygame.font.Font("OCRA.otf", 110)
        s.font2 = pygame.font.Font("OCRA.otf", 20)
        s.last_sync = 0

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
        if time.time() - s.last_sync > SYNCTIME:
            do_sync()
            s.last_sync = time.time()

        s.screen.fill((0, 0, 0))

        t = time.strftime('%H:%M:%S', time.localtime())
        tr = s.font.render(t, True, (0, 255, 0))

        t2 = open("/tmp/ntpsync.txt").readline()
        tt = t2.split()
        if len(tt) == 11:
            t2 = f"       {tt[0]} {tt[1]} {tt[2]} {tt[9]} seconds"
        tr2 = s.font2.render(t2, True, (255, 255, 0))

        s.screen.blit(tr, (0, 0))
        s.screen.blit(tr2, (0, 150))
        pygame.display.flip()

c = sc()
c.run()

