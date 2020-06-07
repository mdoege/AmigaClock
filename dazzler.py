#!/usr/bin/env python

# A kaleidoscope similar to the one for the Cromemco Dazzler (1976)

import pygame
from math import sin, cos, pi
import random, time

RES = 64
RES2 = RES/2
SRES = 640

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

	def events(s):
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

	def run(s):
		s.running = True
		while s.running:
			s.clock.tick(15)
			s.events()
			s.update()
		pygame.quit()

	def draw(s, x, y, c):
		pygame.draw.line(s.dazz, c, (RES2 + x, RES2 + y), (RES2 + x, RES2 + y))
		pygame.draw.line(s.dazz, c, (RES2 - x, RES2 + y), (RES2 - x, RES2 + y))
		pygame.draw.line(s.dazz, c, (RES2 + x, RES2 - y), (RES2 + x, RES2 - y))
		pygame.draw.line(s.dazz, c, (RES2 - x, RES2 - y), (RES2 - x, RES2 - y))

	def update(s):
		if s.paused and not s.step:
			return
		s.step = False
		c = 85*random.randint(0, 3), 85*random.randint(0, 3), 85*random.randint(0, 3)
		if random.random() < random.uniform(.2, 1):
			c = 0, 0, 0
		if random.random() < random.uniform(.01, .03):
			c = 255, 255, 255
		amp = random.gauss(0, .1) + time.time() % 29
		phi = random.gauss(0, .1) + time.time() % 11
		off = random.gauss(0, .3) * sin(time.time()/23)
		if time.time() - s.last > 19:
			s.pow = random.randint(1, 3)
			s.last = time.time()
		for t in range(0, 360, random.randint(1, 3)):
			x = amp * (sin(phi*t*pi/180) + off)**s.pow
			y = amp * (cos(phi*t*pi/180) + off)**s.pow
			s.draw(x, y, c)
			x = 2*amp * (sin(phi*t*pi/180) + off)**s.pow
			y = 2*amp * (cos(phi*t*pi/180) + off)**s.pow
			s.draw(x, y, c)
			x = 3*amp * (sin(phi*t*pi/180) + off)**s.pow
			y = 3*amp * (cos(phi*t*pi/180) + off)**s.pow
			s.draw(x, y, c)

		out = pygame.transform.scale(s.dazz, (s.res))
		s.screen.blit(out, (0, 0))
		
		pygame.display.flip()

c = Dazzler()
c.run()

