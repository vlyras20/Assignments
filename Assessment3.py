import math, random, sys, time
import pygame
from gameSettings import *
from gameSprites import *

pygame.init()
seabg = pygame.image.load('Images/sea.png')
island = pygame.image.load('Images/trees.png')
rod = pygame.image.load('Images/rod.png')
sharkfin = pygame.image.load('Images/sharkfin.png')
music = pygame.mixer.music.load('Audio/main.mp3')

pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

def draw_health(surf, x, y, pct):
	if pct < 0:
		pct = 0
	healthbar_length = 100
	healthbar_height = 20
	fill = pct * healthbar_length
	outline_rect = pygame.Rect(x, y, healthbar_length, healthbar_height)
	fill_rect = pygame.Rect(x, y, fill, healthbar_height)

	if pct > 0.6:
		col = GREEN
	elif pct > 0.3:
		col = YELLOW
	else:
		col = RED
	pygame.draw.rect(surf, col, fill_rect)
	pygame.draw.rect(surf, WHITE, outline_rect, 2)

class Game:
	def __init__(self):
		pygame.init()
		pygame.mixer.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption(TITLE)
		self.clock = pygame.time.Clock()
		self.running = True
		self.font_name = pygame.font.match_font(FONT_NAME)
		self.player = Player()

	def new(self):
		self.all_sprites = pygame.sprite.Group()
		self.fish_sprites = pygame.sprite.Group()
		self.meteors = pygame.sprite.Group()
		self.player = Player()
		self.fish1 = Fish(fish1, 0, 577, 0, 1)
		self.fish2 = Fish(fish2, 960, 554, 0, 0)
		self.fish3 = Fish(fish3, 500, 550, 0, 1)
		self.fish4 = Fish(fish4, 700, 568, 0, 0)
		self.fish5 = Fish(fish5, 50, 500, 0, 1)
		self.fish6 = Fish(fish5, 900, 530, 0, 0)
		self.sharkfin = SharkFin(sharkfin, 960, self.player.pos.y, 0)
		self.rod = Rod(rod, self.player.pos.x, self.player.pos.y)
		self.all_sprites.add(self.player)

		self.fish_sprites.add(self.fish1)
		self.fish_sprites.add(self.fish2)
		self.fish_sprites.add(self.fish3)
		self.fish_sprites.add(self.fish4)
		self.fish_sprites.add(self.fish5)
		self.run()

    # game loop
	def run(self):
		self.playing = True
		for i in range(22):
			m = Meteors()
			self.all_sprites.add(m)
			self.meteors.add(m)
		while self.playing:
			self.clock.tick(FPS)
			self.events()
			self.update()
			self.draw()


    # update part of game loop
	def update(self):
		self.all_sprites.update()
		global bgy
		global islandx
		global waiting
		global spawnMeteors
		global SCORE
		fishspawn = False
		counter = 0

		pygame.sprite.spritecollide(self.rod, self.fish_sprites, True)

		if waiting == False:
			self.player.pos.y -= 1
			bgy -= 1

		if self.player.pos.y  <= HEIGHT * 3 / 4:
			self.player.pos.y = HEIGHT * 3 / 4
			fishspawn = True

		if bgy <= HEIGHT * 3 / 4:
			bgy = HEIGHT * 3 / 4

		if fishspawn == True:
			self.all_sprites.add(self.sharkfin)
			self.all_sprites.add(self.fish1)
			self.all_sprites.add(self.fish2)
			self.all_sprites.add(self.fish3)
			self.all_sprites.add(self.fish4)
			self.all_sprites.add(self.fish5)
			self.all_sprites.add(self.fish6)

		keys = pygame.key.get_pressed()
		if keys[pygame.K_s]:
			# pygame.draw.line(self.screen, BLACK, [self.player.pos.x, self.player.pos.y + 30], [self.player.pos.x, self.player.pos.y + 130], 5)
			self.screen.blit(rod, (self.player.pos.x, self.player.pos.y + 25))
			self.rod.update()

			# fish_col = pygame.sprite.spritecollide(self.rod, self.fish_sprites, False)
			# if fish_col:
			# 	for self.fish in fish_col:
			# 		self.fish.kill()
			pygame.sprite.spritecollide(self.rod, self.fish_sprites, True)
			pygame.display.flip()

		# hit = pygame.sprite.spritecollide(self.rod, self.fish_sprites, False)
		# if hit:
		# 	SCORE += 20
		# 	self.text(TITLE, 48, WHITE, 240, 100)

		hits = pygame.sprite.spritecollide(self.player, self.meteors, False)
		for hit in hits:
			self.player.health -= meteorDMG
			hit.kill()
			if self.player.health <= 0:
				self.playing = False

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
		# self.text('Score: ' + SCORE, 48, WHITE, WIDTH / 2, HEIGHT / 4)
		# self.screen.blit(island,(islandx, islandy))
		self.all_sprites.draw(self.screen)
		draw_health(self.screen, 10, 10, self.player.health / playerHealth)
		pygame.display.flip()

	def titleScreen(self):
		self.screen.fill(BGCOLOR)
		self.text(TITLE, 136, WHITE, (WIDTH/2), (HEIGHT/4))
		self.text('Use [A] and [D] to move', 100, WHITE, WIDTH / 2, HEIGHT / 2)
		self.text('Use [S] to fish', 100, WHITE, WIDTH / 2, HEIGHT / 1.4)
		self.text('Press any key to start', 30, WHITE, WIDTH / 2, HEIGHT / 2.5)
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
		text_rect_x = x
		text_rect_y = y
		text_rect.center = (x, y)
		self.screen.blit(text_surface, text_rect)



g = Game()
g.titleScreen()

# main loop
while g.running:
	g.new()

pygame.quit()
