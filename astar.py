import pygame
import cell

# set up the display
WIDTH = 500
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")


# main function
def main(win, width):
    # make the grid
    ROWS = 50
    grid = cell.make_grid(ROWS, width)

    # define the start and end position
    start = None
    end = None

    run = True
    started = False

    while run:
        # draw everything
        cell.draw(win, grid, ROWS, width)

        # loop through all the events and check what they are
        for event in pygame.event.get():
            # stop running the game if x is pressed
            if event.type == pygame.QUIT:
                run = False

            # if the left mouse button was pressed
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = cell.get_clicked_pos(pos, ROWS, width)
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
                row, col = cell.get_clicked_pos(pos, ROWS, width)

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
                if event.key == pygame.K_SPACE and start and end:
                    # update all neighbours of all the spots
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)
                    
                    # apply the a* algorithm
                    cell.algorithm(lambda: cell.draw(win, grid, ROWS, width), grid, start, end)
                
                # if c is pressed
                if event.key == pygame.K_c:
                    # clear the grid and reset everything
                    start = None
                    end = None
                    grid = cell.make_grid(ROWS, width)

    
    pygame.quit()

main(WIN, WIDTH)


