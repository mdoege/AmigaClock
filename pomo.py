#!/usr/bin/env python

# Activity timer

import pygame, time

class tc:
    def __init__(s):
        pygame.init()
        s.res = 260, 220
        s.screen = pygame.display.set_mode(s.res)
        s.out = pygame.Surface(s.res)
        pygame.display.set_caption("PyModoro")
        s.clock = pygame.time.Clock()
        s.font = pygame.font.Font("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 180)
        s.start = time.time()

    def events(s):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                s.running = False
            # reset timer:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                s.start = time.time()

    def run(s):
        s.running = True
        while s.running:
            s.clock.tick(10)
            s.events()
            s.update()
        pygame.quit()

    def update(s):
        s.screen.fill((255, 255, 255))
        m = ((time.time() - s.start) // 60) % 25    # 25-minute units:
        # 20 minutes green; 5 minutes red
        if m < 20: col = 0, 255, 0
        else:      col = 255, 0, 0
        tr = s.font.render("%02u" % (m + 1), True, col)
        #print(tr.get_size())
        s.screen.blit(tr, ((s.res[0] - tr.get_size()[0]) // 2, 0))
        pygame.display.flip()

c = tc()
c.run()

