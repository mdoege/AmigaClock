#!/usr/bin/env python

# network usage monitor

import pygame, time

BLUE = 0, 85, 170
ORANGE = 255, 136, 0
WHITE = 255, 255, 255
MAX_BPS = 64 * 1024 * 1024 	# maximum line capacity (64 Mbps)
fn = "/sys/class/net/enp23s0/statistics/"

class NetMon:
	def __init__(s):
		pygame.init()
		s.res = 200, 100
		s.screen = pygame.display.set_mode(s.res)
		pygame.display.set_caption('netmon')
		s.screen.fill(BLUE)
		s.clock = pygame.time.Clock()
		s.old = 0
		s.tt = 0

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
		b = int(open(fn + "rx_bytes").read())
		bps = 8 * (b - s.old) / (time.time() - s.tt)
		s.tt = time.time()
		s.old = b
		net = 100 * bps / MAX_BPS
		s.screen.scroll(dx = -1)
		pygame.draw.line(s.screen, BLUE,
			((s.res[0]-1), s.res[1]-1),
			((s.res[0]-1), 0), 1)
		pygame.draw.line(s.screen, ORANGE,
			((s.res[0]-1), s.res[1]-1),
			((s.res[0]-1), s.res[1]-net), 1)
		# 2 MB/s markers
		for q in range(0, int(MAX_BPS), 2 * 8 * 1024 * 1024):
			y = q / MAX_BPS * s.res[1]
			pygame.draw.line(s.screen, WHITE,
				((s.res[0]-1), s.res[1]-y),
				((s.res[0]-1), s.res[1]-y), 1)
		
		pygame.display.flip()

c = NetMon()
c.run()

