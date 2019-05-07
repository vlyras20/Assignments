import pygame
from gameSettings import *
import random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Images/boatIdleLeft.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = pygame.math.Vector2(WIDTH/2, HEIGHT/1.2 + 100)
        self.velocity = pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, 0)
        self.health = playerHealth

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
        self.vel = pygame.math.Vector2(random.randint(1, 3), 0)
        self.flip = 0
        self.player = Player()

    def update(self):
        if self.flip == 0:
            self.pos.x -= 1
        elif self.flip == 1:
            self.pos.x += 1

        self.pos += self.vel
        if self.pos.x < 0:
            self.pos.x = 960
            self.flip = 0
            self.pos.y = random.randint(430, 585)
        elif self.pos.x > 960:
            self.pos.x = 0
            self.flip = 1
            self.pos.y = random.randint(430, 585)
            self.vel = pygame.math.Vector2(random.randint(1, 3), 0)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_s] and self.pos.x == self.player.pos.x:
            self.kill

        self.rect.center = self.pos

    def CollisionTrigger(self, sprite1, sprite2):
        col = pygame.sprite.spritecollide(sprite1, sprite2, True)
        for i in sprite2:
            if col == i:
                col.kill()

class Meteors(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Images/meteor.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.size = self.image.get_size()
        self.speedY = random.randrange(1, 7)
        self.speedX = random.randrange(-2, 2)

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
            self.speedX = random.randrange(-2, 2)

class Rod(pygame.sprite.Sprite):
    def __init__(self,img, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('Images/rod.png')
        self.image = img
        self.rect = self.image.get_rect()
        self.player = Player()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x = self.player.pos.x
        self.rect.y = self.player.pos.y

    def hit(self, fish_sprites):
        return pygame.Rect(self.rect.x, self.rect.y, 77, 77).collidepoint((fish_sprites.x, fish_sprites.y))


class SharkFin(pygame.sprite.Sprite):
    def __init__(self,img, x, y, flip):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('Images/sharkfin.png')
        self.image = img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(random.randint(1, 3), 0)
        self.flip = 0

    def update(self):
        if self.flip == 0:
            self.pos.x -= 1
        elif self.flip == 1:
            self.pos.x += 1

        self.pos += self.vel
        if self.pos.x < 0:
            self.pos.x = 960
            self.flip = 0
            self.pos.y = random.randint(550, 595)
        elif self.pos.x > 960:
            self.pos.x = 0
            self.flip = 1
            pygame.transform.flip(self.image, True, False)
        self.rect.center = self.pos
