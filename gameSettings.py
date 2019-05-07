
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
WIDTH = 960   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 600  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Tony's Ship"
BGCOLOR = SEA

bgx = 0
bgx2 = 480
bgy = 605

islandx = 0
islandy = 400

timer = 0
t = -1
SCORE = 0
meteorDMG = 25
playerHealth = 150

waiting = True
FishingActive = False
spawnMeteors = False

FONT_NAME = 'arial'

obstacles = []

fish1 = 'Images/fish1.png'
fish2 = 'Images/fish2.png'
fish3 = 'Images/fish3.png'
fish4 = 'Images/fish4.png'
fish5 = 'Images/fish5.png'
