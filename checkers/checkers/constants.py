import pygame

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255, 75)
GREY = (105, 105, 105)
YELLOW = (255, 255, 0)

# crown = pygame.transform.scale(pygame.image.load('assets/crown.png'), (45, 25))
CROWN = pygame.image.load('/home/vvander/Documents/Coding/Python/checkers/checkers/assets/crown.png')