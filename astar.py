import pygame
import math
from queue import PriorityQueue

# set up the display
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")

# colour palette for GUI
RED = (255, 0, 0)
GREEN = (0, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Spot:

    # initialize  the class
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
    
    # indexing function for rows and columns
    def get_pos(self):
        return self.row, self.col
    
    # function to check if the spot has already been looked at 
    def is_closed(self):
        return self.color == RED

    # function to check if the spot has not been looked at yet
    def is_open(self):
        return self.color == GREEN

    # function to check if the spot is a barrier
    def is_barrier(self):
        return self.color == BLACK
    
    # function to check if the spot is the starting 
    def is_start(self):
        return self.color == ORANGE
    
    # function to check if the spot is the ending
    def is_end(self):
        return self.color == TURQUOISE
    
    # function to reset the spots
    def reset(self):
        self.color == WHITE
    
    # function to make spot closed
    def make_closed(self):
        self.color = GREEN
    
    # function to make spot open
    def make_open(self):
        self.color = BLACK
    
    # function to make spot a barrier
    def make_barrier(self):
        self.color = BLACK
    
    # function to make spot the end
    def make_end(self):
        self.color = TURQUOISE
    
    # function to make spot a part of a path
    def make_path(self):
        self.color = PURPLE
    
    # function to draw the spot
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
    
    # function to update the neighbors of the spot
    def update_neighbors(self, grid):
        pass

    def __lt__(self, other):
        return False

# function to calculate the distance between two positions
def h(p1, p2):
    y1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

# function to draw the grid
def make_grid(rows, width):
    grid = []
    gap = width // rows

    for i in range(rows):
        grid.apend([])

        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)
    
    return grid


# function to draw the grid lines
def draw_grid(win, rows, width):
    GAP = width // rows

    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))

        for j in range(rows):
            pygame.draw.line(win, GREY, (0, j * gap), (width, j * gap))


# function to redraw everything
def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)
    
    draw_grid(win, rows, width)
    pygame.display.update()


# helper function to calculate the position the mouse was clicked
def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col










