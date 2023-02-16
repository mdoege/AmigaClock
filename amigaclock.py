#!/usr/bin/env python3

# AmigaOS 1.3 clock in PyGame

# inspired by https://www.reddit.com/r/pygame/comments/bdudmf/a_simple_clock/

import pygame
from math import pi, cos, sin
import datetime, os

BLUE = 0, 85, 170
BLACK = 0, 0, 0
WHITE = 255, 255, 255
ORANGE = 255, 136, 0

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

class AmigaClock:
	def __init__(s):
		pygame.init()
		s.res = 250, 250  # default window size
		s.screen = pygame.display.set_mode(s.res, pygame.RESIZABLE)
		pygame.display.set_caption('AmigaClock')
		pygame.display.set_icon(pygame.image.load('amigaclock_icon.png'))
		s.screen.fill(BLUE)
		s.clock = pygame.time.Clock()

	def events(s):
		for event in pygame.event.get():
			if event.type == pygame.QUIT: s.running = False
			if event.type == pygame.VIDEORESIZE:
				s.res = event.w, event.h
				#print(s.res)
				s.screen = pygame.display.set_mode(s.res, pygame.RESIZABLE)

	def run(s):
		s.running = True
		while s.running:
			s.clock.tick(10)
			s.events()
			s.update()
		pygame.quit()

	def clocksize(s):
		return int(.95 * min(s.res)/2)

	def diam(s, x, r1, r2, r3, dx):
		x1, y1 = r1*s.clocksize()*sin(x*pi/180), r1*s.clocksize()*cos(x*pi/180)
		x2, y2 = r2*s.clocksize()*sin((x+dx)*pi/180), r2*s.clocksize()*cos((x+dx)*pi/180)
		x3, y3 = r3*s.clocksize()*sin(x*pi/180), r3*s.clocksize()*cos(x*pi/180)
		x4, y4 = r2*s.clocksize()*sin((x-dx)*pi/180), r2*s.clocksize()*cos((x-dx)*pi/180)
		p = [
			(int(x1+s.res[0]//2), int(-y1+s.res[1]//2)),
			(int(x2+s.res[0]//2), int(-y2+s.res[1]//2)),
			(int(x3+s.res[0]//2), int(-y3+s.res[1]//2)),
			(int(x4+s.res[0]//2), int(-y4+s.res[1]//2)),
		]
		pygame.draw.polygon(s.screen, BLACK, p)

	def update(s):
		s.screen.fill(BLUE)
		pygame.draw.circle(s.screen, BLACK, (s.res[0]//2, s.res[1]//2), s.clocksize())
		pygame.draw.circle(s.screen, WHITE, (s.res[0]//2, s.res[1]//2), int(.98*s.clocksize()))
		for x in range(60):
			x1, y1 = .95*s.clocksize()*sin(6*x*pi/180), .95*s.clocksize()*cos(6*x*pi/180)
			x2, y2 = .88*s.clocksize()*sin(6*x*pi/180), .88*s.clocksize()*cos(6*x*pi/180)
			pygame.draw.line(s.screen, BLACK,
				(int(x1+s.res[0]//2), int(y1+s.res[1]//2)),
				(int(x2+s.res[0]//2), int(y2+s.res[1]//2)), 2)
		for x in range(0, 360, 30):
			s.diam(x, .95, .88, .81, 3)

		# hour hand
		now = datetime.datetime.now()
		x = 30*((now.hour - 12) % 12) + now.minute/2
		s.diam(x, .55, .42, 0, 6)

		# minute hand
		x = 6*now.minute + now.second/10
		s.diam(x, .8, .68, 0, 3)

		# second hand
		x = 6*now.second
		x1, y1 = .8*s.clocksize()*sin(x*pi/180), .8*s.clocksize()*cos(x*pi/180)
		x2, y2 = 0, 0
		pygame.draw.line(s.screen, ORANGE,
			(int(x1+s.res[0]//2), int(-y1+s.res[1]//2)),
			(int(x2+s.res[0]//2), int(-y2+s.res[1]//2)), 2)
		
		pygame.display.flip()

c = AmigaClock()
c.run()

