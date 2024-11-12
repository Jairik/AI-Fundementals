''' Class that holds AI functionality - JJ McCauley - 11/7/24 '''

import numpy as np  # Board calculations
import heapq  # A* Search

class bot:
    
    global TARGETB  # Hold the target board
    global total_cost  # Total cost variable to increment throughout
    global last_cost  # Holds the previous cost to avoid any loops
    
    ''' Initialize variables on create '''
    def __init__(self):
        global total_cost, TARGETB, last_cost
        TARGETB = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])  # Target Board
        total_cost = 0
        last_cost = 999  # Signal Value
    
    '''Calculates Hueristic function based on Manhattan Distance'''
    def hueristic(self, board, x, y):
        global TARGETB
        target_cords = np.where(TARGETB == board[x][y])  # Returns an array of row and column indices found
        print("target cords: ", target_cords)
        # Return manhattan distance
        return (abs(target_cords[0][0] - x) + abs(target_cords[1][0] - y))
    
    '''Gets Adjancent from provided blankspace
    Helper for A* Search, return a list of tuples of adjacent tiles w/ movement vector'''
    def get_adjacent(self, cords: tuple):
        adjacent_cords = []
        if cords[0] < 3: adjacent_cords.append((cords[0]+1, cords[1], (1, 0)))  # Move down
        if cords[0] > 0: adjacent_cords.append((cords[0]-1, cords[1], (-1, 0)))  # Move up
        if cords[1] < 3: adjacent_cords.append((cords[0], cords[1]+1, (0, 1)))  # Move right
        if cords[1] > 0: adjacent_cords.append((cords[0], cords[1]-1, (0, -1)))  # Move left
        return adjacent_cords
    
    '''Calculates next move using A* Search, returning the coordinates of the next 
    Parameters: current board (2d array) and coordinates of blank space'''
    def get_next_move(self, board, cords: tuple):
        print("--BOARD--\n", board, "\n-------")
        global total_cost
        adjacent_cords = self.get_adjacent(cords)  # Get list of tuples of adjacent squares
        adjacent_cords_costs = np.array([])
        total_cost+= 1
        # Simulate the cost of each movement
        for pos in adjacent_cords:
            simulated_board = board.copy()
            x_swap_offset, y_swap_offset = pos[2][0], pos[2][1]  # Coordinates of number to swap with
            # Determine grid position of indexes to swap
            x_swap_cord = pos[0] + x_swap_offset
            y_swap_cord = pos[1] + y_swap_offset
            # Swap given indexes on temporary board
            tempx, tempy = simulated_board[cords[0]], simulated_board[cords[1]]
            simulated_board[cords[0]], simulated_board[cords[1]] = simulated_board[x_swap_cord], simulated_board[y_swap_cord]
            simulated_board[x_swap_cord], simulated_board[y_swap_cord] = tempx, tempy
            hCost = self.hueristic(simulated_board, x_swap_cord, y_swap_cord)  # Get hueristic cost
            adjacent_cords_costs = np.append(adjacent_cords_costs, (hCost + total_cost))
        # Get minimum cost
        min_index = (np.argmin(adjacent_cords_costs))
        # Check for duplicate move to avoid repeating moves
        while adjacent_cords_costs[min_index] == last_cost-1: 
            adjacent_cords_costs = np.delete(adjacent_cords_costs, min_index)
            min_index = (np.argmin(adjacent_cords_costs))
        # Return coordinates to optimal tile to move
        min_i, min_j = adjacent_cords[min_index][0], adjacent_cords[min_index][1]
        print(f"Optimal Indexes to Swap: {min_i}, {min_j}")
        return min_i, min_j