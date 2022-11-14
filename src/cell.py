from queue import PriorityQueue
import pygame

# colour palette for GUI
RED = (160, 160, 245)
GREEN = (113, 113, 227)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (225, 225, 252)
BLACK = (0, 0, 0)
PURPLE = (222, 113, 40)
ORANGE = (255, 36, 189)
GREY = (128, 128, 128)
TURQUOISE = (227, 25, 18)


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
        self.color = RED
    
    # function to make spot open
    def make_open(self):
        self.color = GREEN
    
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
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


# function to draw the shortest path
def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()

# function to implement the a* algorithm
def algorithm(draw, grid, start, end):
    count = 0

    # set of open cells
    open_set = PriorityQueue()
    open_set.put((0, count, start))

    # set of cells previously visited
    came_from = {}

    # g_score is the exact distance travelled so far
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0

    # f_score = g_score + h_score 
    f_score = {spot: float("inf") for row in grid for spot in row}
    # h_score is the heuristic distance from one position to another
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    # keep running until there are not spots in the open set
    while not open_set.empty():
        # get the last event
        for event in pygame.event.get():
            # quit event 
            if event.type == pygame.QUIT:
                pygame.quit
        
        current = open_set.get()[2]
        open_set_hash.remove(current)

        # if the end position is found
        if current == end:
            # construct the shortest path
            reconstruct_path(came_from, end, draw)
            return True
        
        # traverse through the neighbors
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            # if current path is shorter
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                # corrent g_score is recorded
                g_score[neighbor] = temp_g_score
                # f_score is calculated
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())

                if neighbor not in open_set_hash:
                    # increase the count
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    # add neighbour to the set
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        
        # redraw everything
        draw()
        
        if current != start:
            current.make_closed()
    
    return False

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
