#!/usr/bin/env python

# Uptime clock

import pygame, time

class tc:
    def __init__(s):
        pygame.init()
        s.res = 631, 91
        s.screen = pygame.display.set_mode(s.res)
        s.out = pygame.Surface(s.res)
        pygame.display.set_caption("Uptime Clock")
        s.clock = pygame.time.Clock()
        s.font = pygame.font.Font("/usr/share/fonts/TTF/IBMPlexSans-SemiBold.ttf", 70)
        s.last = 0

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
        if time.time() - s.last > 30:
            s.uptime = float(open("/proc/uptime").readline().split()[0])
            s.last = time.time()
        s.screen.fill((0, 0, 0))

        ui = int(s.uptime / 60)
        uh, um = divmod(ui, 60)
        if uh < 1:
            t = f"uptime: {um} m"
        else:
            t = f"uptime: {uh} h, {um} m"
        tr = s.font.render(t, True, (0, 255, 0))
        #print(tr.get_size())
        s.screen.blit(tr, (0, 0))
        pygame.display.flip()

c = tc()
c.run()

