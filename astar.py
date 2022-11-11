import pygame
import math
from queue import PriorityQueue

# set up the display
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
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
        self.color = WHITE
    
    # function to make spot closed
    def make_closed(self):
        self.color = GREEN
    
    # function to make spot open
    def make_open(self):
        self.color = BLACK
    
    # function to make spot a barrier
    def make_barrier(self):
        self.color = BLACK
    
    # function to make the spot end
    def make_start(self):
        self.color = ORANGE
    
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
        self.neighbors = []

        # add bottom neighbour
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])
        
        # add top neighbour
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])
        
        # add right neighbour
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])
        
        # add left neighbour
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])
        

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
        grid.append([])

        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)
    
    return grid


# function to draw the grid lines
def draw_grid(win, rows, width):
    gap = width // rows

    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))

        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


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


# main function
def main(win, width):
    # make the grid
    ROWS = 50
    grid = make_grid(ROWS, width)

    # define the start and end position
    start = None
    end = None

    run = True
    started = False

    while run:
        # draw everything
        draw(win, grid, ROWS, width)

        # loop through all the events and check what they are
        for event in pygame.event.get():
            # stop running the game if x is pressed
            if event.type == pygame.QUIT:
                run = False
            
            # if the alrogithm has started, all other acitions are ignored
            if started:
                continue

            # if the left mouse button was pressed
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]

                # if click did not set start position
                if not start and spot != end:
                    # set start position
                    start = spot
                    start.make_start()
                
                # if click did not set end position
                elif not end and spot != start:
                    # set end position
                    end = spot
                    end.make_end()

                # if click did not set start of end position
                elif spot != end and spot != end:
                    # create a barrier
                    spot.make_barrier()         

            # if the right mouse button was pressed
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)

                # erase whatever is clicked
                spot = grid[row][col]
                spot.reset()

                # erase the start position
                if spot == start:
                    start = None
                
                # erase the end position
                elif spot == end:
                    end = None
            
            # if a key has been pressed
            if event.type == pygame.KEYDOWN:
                # if the spacebar was pressed and algorithm has not started yet
                if event.key == pygame.K_SPACE and not started:
                    # update all neighbours of all the spots
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors()
                    
                    algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)

    
    pygame.quit()

main(WIN, WIDTH)










