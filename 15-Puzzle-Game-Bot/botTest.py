from bot import bot

b_pos = (0, 1)
bot = bot()  # Make a new bot object

def run_bot(board, moves_label):    
    global b_pos
    
    # Define a function for each iteration of the bot's movement
    def bot_iteration(board):
        global b_pos
        #print("\n\nExecuting Bot Iteration #", move_count)
        print("Original Board: ", board, "\n")
        # Get the optimal move from the bot. Will update board within function (by reference)
        b_pos, board = bot.make_next_move(board, b_pos)
        print("Blank position After Make_Next_Move function: ", b_pos)
        print("New board: ", board, "\n")
        
        # Increment move counter and update the GUI
        #move_count += 1
        #moves_label.setText(f"Moves Made: {move_count}")
        temp = input("\nEnter any character to continue...")
        print()  # Empty line
        bot_iteration(board)
        
    # Start the bot iteration
    bot_iteration(board)
    
    
'''Testing logic'''
board = [[1, 0, 2, 3], [5, 6, 7, 4], [9, 10, 11, 8], [13, 14, 15, 12]]  # Hardcoded test case
run_bot(board, None)