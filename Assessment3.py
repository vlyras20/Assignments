import math, random, sys
import pygame
from gameSettings import *
from gameSprites import *

class Game:
	def __init__(self):
		pygame.init()
		pygame.mixer.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption(TITLE)
		self.clock = pygame.time.Clock()
		self.running = True

	def new(self):
		self.all_sprites = pygame.sprite.Group()
		self.player = Player()
		self.all_sprites.add(self.player)
		self.run()

    # game loop - set self.playing = False to end the game
	def run(self):
		self.playing = True
		while self.playing:
			self.clock.tick(FPS)
			self.events()
			self.update()
			self.draw()

    # update portion of the game loop
	def update(self):
		self.all_sprites.update()
		if self.player.rect.top <= HEIGHT / 2:
			self.player.velocity.y = 0
			self.player.pos.y += abs(self.player.velocity.y)

	# exit the program
	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				if self.playing:
					self.playing = False
				self.running = False


	def draw(self):
		self.screen.fill(SEA)
		self.screen.blit(seabg,(bgx, 505))
		self.all_sprites.draw(self.screen)
		pygame.display.flip()

	def titleScreen(self):
		pass

g = Game()
g.titleScreen()

seabg = pygame.image.load('Images/sea.png')
bgx = 0

# main loop
while g.running:
	g.new()
	g.titleScreen()


pygame.quit()
	# pygame.draw.circle(DS, WHITE, (int(circlePosX), playerPosY - circleRadius), circleRadius, 0)
