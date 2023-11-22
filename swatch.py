#!/usr/bin/env python

# Swatch internet clock

import pygame

# https://gist.github.com/AledDavies/2a37b9a6d427da2bc4a0b001dee2377d

# (modified for precision)

from datetime import datetime, timezone

def now():
    now = datetime.now(timezone.utc)

    # we need to convert the supplied time to CET to calculate
    # the beats.
    seconds = (3600+(now.hour * 3600) +
              (now.minute*60) +
              (now.second) + 1e-6 * now.microsecond) % 86400

    # Round off to 3 decimal places
    return round(seconds / 86.4, 3)

class sc:
    def __init__(s):
        pygame.init()
        s.res = 640, 145
        s.screen = pygame.display.set_mode(s.res)
        s.out = pygame.Surface(s.res)
        pygame.display.set_caption("Swatch Clock")
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

        tr = s.font.render("@%7.3f" % now(), True, (0, 255, 255))
        #print(tr.get_size())
        s.screen.blit(tr, (0, 0))
        pygame.display.flip()

c = sc()
c.run()

