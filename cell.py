#!/usr/bin/env python

# Cellular automaton
#   (press Space to pick a new rule, color scheme, and initial conditions)

import pygame, random

def getcol():
    return [85 * random.randint(0, 3) for q in (1, 2, 3)]

COL = getcol(), getcol()
FPS = 60
RULES = 18, 22, 26, 30, 41, 45, 54, 60, 90, 102, 105, 106, 110, 122, 126, 146, 150, 154, 182
RES = 500, 300
PIXSIZE = 2
NCELL = RES[0] // PIXSIZE

class Cell:
    def __init__(self):
        pygame.init()
        self.res = int(2 * RES[0]), int(2 * RES[1])
        self.screen = pygame.display.set_mode(self.res, pygame.RESIZABLE)
        pygame.display.set_caption('cell')
        self.clock = pygame.time.Clock()
        self.newrule()

    def newrule(self):
        global COL

        COL = getcol(), getcol()
        if random.random() < .5:
            self.cell = [random.randint(0, 1) for q in range(2 + NCELL)]
        else:
            self.cell = [0 for q in range(2 + NCELL)]
            for n in range(random.randint(1, 10)):
                self.cell[random.randint(10, NCELL-10)] = 1
        self.rule = random.choice(RULES)
        self.gen = 1
        self.line = 0

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: self.running = False
            if event.type == pygame.VIDEORESIZE:
                self.res = event.w, event.h
                self.screen = pygame.display.set_mode(self.res, pygame.RESIZABLE)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.newrule()

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
        pygame.quit()

    def newgen(self):
        self.gen += 1
        cell2 = [0 for q in range(2 + NCELL)]
        for x in range(NCELL):
            s = 2 ** (4 * self.cell[x] + 2 * self.cell[x + 1] + self.cell[x + 2])
            if s & self.rule:
                cell2[x + 1] = 1
        # make cyclic
        cell2[0] = cell2[-2]
        cell2[-1] = cell2[1]
        self.cell = cell2

    def update(self):
        self.line += 1
        #print(self.line, self.gen)
        self.screen.scroll(dy = -1)
        pygame.draw.line(self.screen, (0, 0, 0),
            (0, self.res[1]-1),
            (self.res[0]-1, self.res[1]-1), 1)
        scrollfac = max(1, int(self.res[0] / RES[0]))
        if (self.line / PIXSIZE) % scrollfac == 0:
            self.newgen()
        for x in range(self.res[0]):
            xp = int(x / self.res[0] * NCELL)
            pygame.draw.line(self.screen, COL[self.cell[xp + 1]],
                (x, self.res[1]-1),
                (x, self.res[1]-1), 1)
        pygame.display.set_caption('cell (rule %u)' % self.rule)
        
        pygame.display.flip()

c = Cell()
c.run()

