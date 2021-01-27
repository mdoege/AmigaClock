#!/usr/bin/env python

# "Munching squares"

import pygame
from math import sin, cos, pi
import random, time

RES = 128
RES2 = RES/2
SRES = 640
tile = 1		# number of tiles (press T to change)
slow = False		# slow mode (press S to toggle)

def ttime():
	if slow:
		return .5 * time.time()
	else:
		return time.time()

class Dazzler:
	def __init__(s):
		pygame.init()
		s.res = SRES, int(0.75 * SRES)
		s.screen = pygame.display.set_mode(s.res, pygame.RESIZABLE)
		pygame.display.set_caption('Dazzler')
		s.clock = pygame.time.Clock()
		s.dazz = pygame.Surface((RES, RES))
		s.pow = 1
		s.last = 0
		s.paused = False
		s.step = False
		s.t = 0

	def events(s):
		global tile, slow

		for event in pygame.event.get():
			if event.type == pygame.QUIT: s.running = False
			if event.type == pygame.VIDEORESIZE:
				s.res = event.w, event.h
				#print(s.res)
				s.screen = pygame.display.set_mode(s.res, pygame.RESIZABLE)
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				s.paused = not s.paused
			if event.type == pygame.KEYDOWN and event.key == pygame.K_PERIOD:
				s.step = True
			if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
				tile += 1
				if tile > 5:
					tile = 1
			if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
				slow = not slow

	def run(s):
		s.running = True
		while s.running:
			if slow:
				s.clock.tick(8)
			else:
				s.clock.tick(15)
			s.events()
			s.update()
		pygame.quit()

	def draw(s, x, y, c):
		pygame.draw.line(s.dazz, c, (RES2 + x, RES2 + y), (RES2 + x, RES2 + y))
		pygame.draw.line(s.dazz, c, (RES2 - x, RES2 + y), (RES2 - x, RES2 + y))
		pygame.draw.line(s.dazz, c, (RES2 + x, RES2 - y), (RES2 + x, RES2 - y))
		pygame.draw.line(s.dazz, c, (RES2 - x, RES2 - y), (RES2 - x, RES2 - y))

	def draw2(s, x, y, c):
		pygame.draw.line(s.dazz, c, (x, y), (x, y))

	def update(s):
		if s.paused and not s.step:
			return
		s.t += 1
		if s.t > RES:
		    s.t = 0
		c = 85*random.randint(0, 3), 85*random.randint(0, 3), 85*random.randint(0, 3)
		if random.random() < random.uniform(.2, 1):
			c = 0, 0, 0
		if random.random() < random.uniform(.01, .03):
			c = 255, 255, 255
			
		for x in range(RES):
			y = x ^ s.t
			s.draw2(x, y, c)

		tres = s.res[0] // tile, s.res[1] // tile
		out = pygame.transform.scale(s.dazz, tres)
		for y in range(tile):
			for x in range(tile):
				s.screen.blit(out, (tres[0] * x, tres[1] * y))
		
		pygame.display.flip()

c = Dazzler()
c.run()

