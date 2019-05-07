import math, random, sys
import pygame
from gameSettings import *
from gameSprites import *

seabg = pygame.image.load('Images/sea.png')
island = pygame.image.load('Images/trees.png')
rod = pygame.image.load('Images/fishingrod1.png')

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
		self.fish_sprites = pygame.sprite.Group()
		self.meteors = pygame.sprite.Group()
		self.player = Player()
		self.fish1 = Fish(fish1, 0, 577, 0, 1)
		self.fish2 = Fish(fish2, 960, 580, 0, 0)
		self.fish3 = Fish(fish3, 500, 550, 0, 1)
		self.fish4 = Fish(fish4, 700, 568, 0, 0)
		self.fish5 = Fish(fish5, 50, 592, 0, 0)
		self.all_sprites.add(self.player)
		self.run()

    # game loop - set self.playing = False to end the game
	def run(self):
		self.playing = True
		for i in range(10):
			m = Meteors()
			self.all_sprites.add(m)
			self.meteors.add(m)

		keys = pygame.key.get_pressed()
		if keys[pygame.K_s]:
			pygame.draw.line(self.screen, BLACK, [0, 0], [0, 0], 5)
		while self.playing:
			self.clock.tick(FPS)
			self.events()
			self.update()
			self.draw()


    # update portion of the game loop
	def update(self):
		self.all_sprites.update()
		global bgy
		global islandx
		global waiting
		global spawnMeteors
		global score
		fishspawn = False
		counter = 0

		if waiting == False:
			self.player.pos.y -= 1
			bgy -= 1
			spawnMeteors = True

		if self.player.pos.y  <= HEIGHT * 3 / 4:
			self.player.pos.y = HEIGHT * 3 / 4
			fishspawn = True
			self.screen.blit(island,(islandx, islandy))
			islandx += 1

		if islandx <= 0:
			islandx = 0

		if bgy <= HEIGHT * 3 / 4:
			bgy = HEIGHT * 3 / 4

		if fishspawn == True:
			self.all_sprites.add(self.fish1)
			self.all_sprites.add(self.fish2)
			self.all_sprites.add(self.fish3)
			self.all_sprites.add(self.fish4)
			self.all_sprites.add(self.fish5)

		hit = pygame.sprite.spritecollide(self.player, self.meteors, False)
		if hit:
			SCORE -= 10
	# exit the program
	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				if self.playing:
					self.playing = False
				self.running = False

	def draw(self):
		self.screen.fill(SEA)
		self.screen.blit(seabg,(bgx, bgy))
		self.screen.blit(seabg,(bgx2, bgy))
		self.text('Score: ' + SCORE, 48, WHITE, WIDTH / 2, HEIGHT / 4)
		self.all_sprites.draw(self.screen)
		pygame.display.flip()

	def titleScreen(self):
		self.screen.fill(BGCOLOR)
		self.text(TITLE, 48, WHITE, 240, 100)
		self.text('Press any key to start', 22, WHITE, 480, 600)
		pygame.display.flip()
		self.waitforTitle()

	def waitforTitle(self):
		global waiting
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



g = Game()
g.titleScreen()

# main loop
while g.running:
	g.new()

pygame.quit()
	# pygame.draw.circle(DS, WHITE, (int(circlePosX), playerPosY - circleRadius), circleRadius, 0)
