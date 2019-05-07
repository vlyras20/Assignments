import pygame
from gameSettings import *
import random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Images/boatIdleLeft.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = pygame.math.Vector2(WIDTH/2, HEIGHT/1.2)
        self.velocity = pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, 0)

    def update(self):
        self.acceleration = pygame.math.Vector2(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.acceleration.x = -0.5
            self.image = pygame.image.load('Images/boatMoveLeft.png')
            playerVelocityX = -1
        elif keys[pygame.K_d]:
            self.acceleration.x = 0.5
            self.image = pygame.image.load('Images/boatMoveRight.png')
            playerVelocityX = 1
        else:
            self.image = pygame.image.load('Images/boatIdleLeft.png')
            playerVelocityX = 0

        self.acceleration += self.velocity * -0.09
        self.velocity += self.acceleration
        self.pos += self.velocity + 0.5 * self.acceleration
        if self.pos.x > 935:
            self.pos.x = 935
        elif self.pos.x < 30:
            self.pos.x = 30

        self.rect.center = self.pos

class Fish(pygame.sprite.Sprite):
    def __init__(self, img, x, y, end, flip):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = pygame.math.Vector2(x, y)
        self.x = x
        self.y = y
        self.end = end
        self.path = [self.x, self.end]
        self.vel = 3
        self.flip = 0

    def update(self):

        if self.flip == 0:
            self.pos.x -= 1
        elif self.flip == 1:
            self.pos.x += 1
            pygame.transform.flip(self.image, True, False)

        if self.pos.x < 0:
            self.pos.x = 960
            self.flip = 0
            self.pos.y = random.randint(550, 595)
        elif self.pos.x > 960:
            self.pos.x = 0
            self.flip = 1
            self.pos.y = random.randint(550, 595)

        self.rect.center = self.pos

class Meteors(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Images/meteor.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedY = random.randrange(1, 7)
        self.speedX = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedX
        self.rect.y += self.speedY
        if self.rect.top > HEIGHT * 3 / 4:
            self.image = pygame.image.load('Images/meteor2.png')
            self.speedY = random.randrange(1, 2)
            self.speedX = 0
        if self.rect.top > HEIGHT + 10 or self.rect.left < -30 or self.rect.right > WIDTH + 20:
            self.image = pygame.image.load('Images/meteor.png')
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedY = random.randrange(1, 7)
            self.speedX = random.randrange(-3, 3)
