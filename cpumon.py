#!/usr/bin/env python

# CPU usage monitor

import pygame, psutil

BLUE = 0, 85, 170
ORANGE = 255, 136, 0

class CPUMon:
	def __init__(s):
		pygame.init()
		s.res = 200, 100
		s.screen = pygame.display.set_mode(s.res)
		pygame.display.set_caption('cpumon')
		s.screen.fill(BLUE)
		s.clock = pygame.time.Clock()

	def events(s):
		for event in pygame.event.get():
			if event.type == pygame.QUIT: s.running = False

	def run(s):
		s.running = True
		while s.running:
			s.clock.tick(4)
			s.events()
			s.update()
		pygame.quit()

	def update(s):
		cpu = int(psutil.cpu_percent(interval=None))
		s.screen.scroll(dx = -1)
		pygame.draw.line(s.screen, BLUE,
			((s.res[0]-1), s.res[1]-1),
			((s.res[0]-1), 0), 1)
		pygame.draw.line(s.screen, ORANGE,
			((s.res[0]-1), s.res[1]-1),
			((s.res[0]-1), s.res[1]-cpu), 1)
		
		pygame.display.flip()

c = CPUMon()
c.run()

