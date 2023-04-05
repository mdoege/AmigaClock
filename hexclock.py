#!/usr/bin/env python

# Hex color clock
# inspired by https://github.com/tidbyt/community/blob/main/apps/hexcolorclock/hex_color_clock.star

import pygame, datetime

class tc:
    def __init__(s):
        pygame.init()
        s.res = 640, 245
        s.screen = pygame.display.set_mode(s.res)
        s.out = pygame.Surface(s.res)
        pygame.display.set_caption("Hex Clock")
        s.clock = pygame.time.Clock()
        s.font = pygame.font.Font("OCRA.otf", 110)
        s.font2 = pygame.font.Font("OCRA.otf", 80)

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
        now = datetime.datetime.now()
        h, m, ss = now.hour, now.minute, now.second

        bb = int(255 * ss / 60)
        gg = int(255 * (m + ss / 60) / 60)
        rr = int(255 * (h + m / 60 + ss / 60 / 60) / 24)
        col = "#%02x%02x%02x" % (rr, gg, bb)
        col2 = "#%02x%02x%02x" % (255-rr, 255-gg, 255-bb)

        s.screen.fill(col)
        t = '%02u:%02u:%02u' % (h, m, ss)
        tr = s.font.render(t, True, col2)
        s.screen.blit(tr, (0, 0))
        tr = s.font2.render(col, True, col2)
        s.screen.blit(tr, (110, 130))
        pygame.display.flip()

c = tc()
c.run()

