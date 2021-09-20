#!/usr/bin/env python

# Wallpaper
# from The New Turing Omnibus: Sixty-Six Excursions in Computer Science

import pygame
import random, time

RES = 100
RES2 = RES/2
SRES = 600
tile = 1		# number of tiles (press T to change)
slow = False		# slow mode (press S to toggle)

def ttime():
	if slow:
		return .5 * time.time()
	else:
		return time.time()


# Amstrad CPC palette
pal = []
for r in range(0, 3):
	for g in range(0, 3):
		for b in range(0, 3):
			pal.append([127 * r, 127 * g, 127 * b])

# RGB, CMY palette
f,h =255,255
pal2 = (
[0,0,f],
[f,0,0],
[h,0,h],
[0,f,0],
[0,h,h],
[h,h,0],
)

class Dazzler:
	def __init__(s):
		pygame.init()
		s.res = SRES, int(0.75 * SRES)
		s.screen = pygame.display.set_mode(s.res, pygame.RESIZABLE)
		pygame.display.set_caption('Wallpaper')
		s.clock = pygame.time.Clock()
		s.dazz = pygame.Surface((RES, RES))
		s.pow = 1
		s.last = 0
		s.paused = False
		s.step = False

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
				s.clock.tick(.1)
			else:
				s.clock.tick(.3)
			s.events()
			s.update()
		pygame.quit()

	def update(s):
		if s.paused and not s.step:
			return
		s.step = False

		corna, cornb, side = (random.randint(0, 50),
						      random.randint(0, 50),
						      random.randint(1, 500))
		#random.shuffle(pal)
		for i in range(RES):
			for j in range(RES):
				x = corna + i*side/RES
				y = cornb + j*side/RES
				c1 = int(x*x+y*y)
				c2 = pal[c1 % len(pal)]
				pygame.draw.line(s.dazz, c2, (i,j), (i,j))

		tres = s.res[0] // tile, s.res[1] // tile
		out = pygame.transform.scale(s.dazz, tres)
		for y in range(tile):
			for x in range(tile):
				s.screen.blit(out, (tres[0] * x, tres[1] * y))
		
		pygame.display.flip()

c = Dazzler()
c.run()

