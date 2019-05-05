# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
SEA = (35, 161, 193)

# game settings
WIDTH = 480   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 600  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "TonyTone"
BGCOLOR = DARKGREY

stagePosX = 0
startScrollingPosX = WIDTH/2

circleRadius = 30
circlePosX = circleRadius

playerPosX = circleRadius
playerVelocityX = 0
