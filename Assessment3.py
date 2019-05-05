import math, random, sys
import pygame
from gameSettings import *
from gameSprites import *

seabg = pygame.image.load('Images/sea.png')

obstacles = []

class Game:
	def __init__(self):
		pygame.init()
		pygame.mixer.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption(TITLE)
		self.clock = pygame.time.Clock()
		self.running = True
		self.font_name = pygame.font.match_font(FONT_NAME)

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
		# if self.player.rect.top <= HEIGHT / 2:
		# 	self.player.velocity.y = 0
		# 	self.player.pos.y += abs(self.player.velocity.y)
		# obstacles.append(FallingObstacles())
		i = 0
		while i < len(obstacles):
			obstacles[i].move()
			obstacles[i].draw()
			if obstacles[i].ypos > 560:
				del obstacles[i]
				i -= 1
			i += 1

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
		self.screen.fill(BGCOLOR)
		self.text(TITLE, 48, WHITE, 240, 100)
		self.text('Press any key to start', 22, WHITE, 240, 300)
		pygame.display.flip()
		self.waitforTitle()

	def waitforTitle(self):
		waiting = True
		while waiting:
			self.clock.tick(FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					waiting = False
					self.running = False
				if event.type == pygame.KEYUP:
					waiting = False

	def text(self, text, size, colour, x, y):
		font = pygame.font.Font(self.font_name, size)
		text_surface = font.render(text, True, colour)
		text_rect = text_surface.get_rect()
		self.screen.blit(text_surface, text_rect)

class FallingObstacles:
    def __init__(self):
        self.xpos = random.randint(0, 480)
        self.ypos = 0
        self.size = random.randint(1, 2)
        self.image = pygame.image.load('Images/meteor.png')
        self.game = Game()

    def draw(self):
        pygame.draw.circle(self.game.screen, (222, 222, 222), (self.xpos, self.ypos), self.size, self.size)

    def move(self):
        self.ypos += random.randint(3, 10)

g = Game()
g.titleScreen()

# main loop
while g.running:
	g.new()

pygame.quit()
	# pygame.draw.circle(DS, WHITE, (int(circlePosX), playerPosY - circleRadius), circleRadius, 0)
