import pygame
from gameSettings import *

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
        if keys[pygame.K_LEFT]:
            self.acceleration.x = -0.5
            self.image = pygame.image.load('Images/boatMoveLeft.png')
            playerVelocityX = -1
        elif keys[pygame.K_RIGHT]:
            self.acceleration.x = 0.5
            self.image = pygame.image.load('Images/boatMoveRight.png')
            playerVelocityX = 1
        else:
            self.image = pygame.image.load('Images/boatIdleLeft.png')
            playerVelocityX = 0

        self.acceleration += self.velocity * -0.09
        self.velocity += self.acceleration
        self.pos += self.velocity + 0.5 * self.acceleration
        self.pos.x = playerPosX
        self.velocity.x = playerVelocityX
        # if self.pos.x > 455:
        #     self.pos.x = 455
        # elif self.pos.x < 30:
        #     self.pos.x = 30

        # self.pos.y -= currentYvelocity
        self.rect.center = self.pos

# class Sea(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load('Images/sea.png')
#         # self.image.fill(YELLOW)
#         self.rect = self.image.get_rect()
#         self.rect.center = (WIDTH/2, HEIGHT/2)
#         self.pos = pygame.math.Vector2(WIDTH/2, HEIGHT/2)
