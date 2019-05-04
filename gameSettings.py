# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "TonyTone"
BGCOLOR = DARKGREY


TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE


# define display surface
W, H = 615, 615
HW, HH = W / 2, H / 2
AREA = W * H


bg = pygame.image.load("Images/grass.jpg")
currentbg = 10
bgWidth, bgHeight = bg.get_rect().size

playerImages = ['Images/1.png','Images/2.png','Images/3.png','Images/4.png','Images/5.png','Images/6.png','Images/7.png','Images/8.png','Images/9.png']

stageWidth = bgWidth * currentbg
stagePosX = 0

startScrollingPosX = HW

circleRadius = 25
circlePosX = circleRadius

playerPosX = circleRadius
playerPosY = 500
playerVelocityX = 0
