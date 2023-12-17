# Duffing oscillator phase space plots
#   horizontal axis = position x
#   vertical axis = velocity v
#   (at the beginning of a run, x=0 and v=0)
#   https://en.wikipedia.org/wiki/Duffing_equation

import pygame, time
from random import uniform, randint
from math import pi, sin

FPS = 30        # frame rate
ts = 20 * FPS   # new plot every 20 s
dt = .08        # time step size
SCALEPARAM = 4  # axis scaling
LW = 4          # line width
FIXPARA = False # use fixed oscialltor parameters and run indefinitely
if FIXPARA: LW = 1

class Duffing:
    def __init__(s):
        pygame.init()
        s.res = 1200, 980  # default window size
        s.screen = pygame.display.set_mode(s.res, pygame.RESIZABLE)
        pygame.display.set_caption('Duffing')
        s.clock = pygame.time.Clock()
        s.newplot()

    def newplot(s):
        "Set up new plot"
        s.screen.fill((0, 0, 0))
        s.color = 51*randint(2, 4), 51*randint(2, 4), 51*randint(2, 4)
        s.x, s.v, s.t = 0, 0, 0
        s.oldx, s.oldy = s.res[0]//2, s.res[1]//2
        s.alpha = uniform(.5, 2)
        s.beta = uniform(.5, 2)
        s.gamma = uniform(1, 5)
        s.delta = uniform(.005, .1)
        s.omega = uniform(.1, .5)

        if FIXPARA:
            para = "1.9180568571216652 1.336766552725862 3.311497074389515 0.07309502896720854 0.4168105372177534"
            s.alpha, s.beta, s.gamma, s.delta, s.omega = [float(q) for q in para.split()]
            s.color = 200, 200, 200

        print(s.alpha, s.beta, s.gamma, s.delta, s.omega)

    def events(s):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: s.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                pygame.image.save(s.screen,
                        time.strftime("duff-%y%m%d_%H%M%S.png"))
            if event.type == pygame.VIDEORESIZE:
                s.res = event.w, event.h
                s.screen = pygame.display.set_mode(s.res, pygame.RESIZABLE)

    def run(s):
        s.running = True
        while s.running:
            s.clock.tick(FPS)
            s.events()
            s.update()
        pygame.quit()

    def update(s):
        if s.t > ts and not FIXPARA:
            s.newplot()
        a = -s.alpha * s.x - s.beta * s.x**3 - s.delta * s.v + s.gamma * sin(s.omega * s.t * dt)
        s.v += dt * a
        s.x += dt * s.v
        s.t += 1

        scale = s.res[0] / SCALEPARAM
        newx, newy = scale * s.x + s.res[0]//2, -scale * s.v + s.res[1]//2
        pygame.draw.line(s.screen, s.color, (s.oldx, s.oldy), (newx, newy), LW)
        s.oldx, s.oldy = newx, newy
        pygame.display.flip()

c = Duffing()
c.run()

