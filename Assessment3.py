import math, random, sys
import pygame
from pygame.locals import *
from gameSettings import *
from gameSprites import *

class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption(TITLE)
		self.clock = pg.time.Clock()
		pygame.key.set_repeat(500, 100)

    # game loop - set self.playing = False to end the game
    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    # update portion of the game loop
    def update(self):
        self.all_sprites.update()

	# exit the program
	def events():
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()

    def titleScreen(self):
        pass

g = Game()
g.titleScreen()

# main loop
while True:
	g.run()

	key = pygame.key.get_pressed()
	if key[K_UP]:
		playerPosY -= 5
	if key[K_DOWN]:
		playerPosY += 5
	if key[K_RIGHT]:
		playerVelocityX = 5
	elif key[K_LEFT]:
		playerVelocityX = -5
	else:
		playerVelocityX = 0

	playerPosX += playerVelocityX
	if playerPosX > stageWidth - circleRadius:
		playerPosX = stageWidth - circleRadius
	if playerPosX < circleRadius:
		playerPosX = circleRadius
	if playerPosX < startScrollingPosX:
		circlePosX = playerPosX
	elif playerPosX > stageWidth - startScrollingPosX:
		circlePosX = playerPosX - stageWidth + W
	else:
		circlePosX = startScrollingPosX
		stagePosX += -playerVelocityX

	rel_x = stagePosX % bgWidth
	DS.blit(bg, (rel_x - bgWidth, 0))
	if rel_x < W:
		DS.blit(bg, (rel_x, 0))

	pygame.draw.circle(DS, WHITE, (int(circlePosX), playerPosY - circleRadius), circleRadius, 0)

	pygame.display.update()
	CLOCK.tick(FPS)
	DS.fill(BLACK)
