''' Class that holds AI functionality - JJ McCauley - 11/7/24 '''

import numpy as np  # Board calculations
import heapq  # A* Search

class bot:
    
    TARGETB = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])  # Target Board
    total_cost = 0 # Cost function, simple counter 
    
    # Any initialization stuff
    def __init__(self):
        total_cost = 0
    
    # Calculate the heuristic (Manhattan Distance) for given coordinates
    def hueristic(self, board, x, y):
        val = board[cords[0]][cords[1]]  # Get the current value from the coordinates
        target_cords = np.where(TARGETB == val)  # Returns an array of row and column indices found
        # Return manhattan distance
        return (abs(target_cords[0][0] - x) + abs(target_cords[1][0] - y))
    
    # Helper for A* Search, return a list of tuples of adjacent nodes w/ movement details
    def get_adjacent(self, board, cords):
        aCords = []
        if cords[0] < 3: aCords.append((cords[0]+1, cords[1], (1, 0)))
        if cords[0] > 0: aCords.append((cords[0]-1, cords[1], (-1, 0)))
        if cords[1] < 3: aCords.append((cords[0], cords[1]+1, (0, 1)))
        if cords[1] > 0: aCords.append((cords[0], cords[1]-1, (0, -1)))
        return aCords
    
    # Calculates next move using A* Search, returning the coordinates of the next 
    # Parameters: current board (2d array) and coordinates of blank space
    def ASearch(self, board, cords: tuple):
        aCords = get_adjacent(board, cords)  # Get list of tuples of adjacent squares
        aCord_costs = np.array([])
        total_cost += 1
        # Simulate the cost of each movement
        for cur_cords in aCords:
            simulated_board = board.copy()
            x_swap_cord, y_swap_cord = cur_cords[2][0], cur_cords[2][1]  # Coordinates of number to swap with
            # Swap the numbers on the simulated board
            simulated_board[cords[0]][cords[1]], simulated_board[x_swap_cord], simulated_board[y_swap_cord] = \
                simulated_board[x_swap_cord], simulated_board[y_swap_cord], simulated_board[cords[0]][cords[1]]
            hCost = hueristic(simulated_board, x_swap_cord, y_swap_cord)  # Get hueristic cost
            aCord_costs = np.append(aCord_costs, (hCost + total_cost))
        min_i, min_j = np.unravel_index((np.argmin(aCord_costs)), aCord_costs.shape)
        print("Optimal Indexes to Swap: {min_i}, {min_j}")
        return min_i, min_j