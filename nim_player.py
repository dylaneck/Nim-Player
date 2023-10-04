'''
This class is used to play the game of nim. It uses the nim sum to calculate the best move for the given game state.
'''
class NimPlayer():
    def __init__(self):
        pass
    
    def calculate_binary(self, nim_board):
        # Creates list of binary digits for each possible value in the nim board
        bin_list = []
        for row in nim_board:
            if row == 0:
                bin_list.append([0, 0, 0])
            elif row == 1:
                bin_list.append([0, 0, 1])
            elif row == 2:
                bin_list.append([0, 1, 0])
            elif row == 3:
                bin_list.append([0, 1, 1])
            elif row == 4:
                bin_list.append([1, 0, 0])
            elif row == 5:
                bin_list.append([1, 0, 1])
            elif row == 6:
                bin_list.append([1, 1, 0])
            elif row == 7:
                bin_list.append([1, 1, 1])            
            
        return bin_list
    
    def nim_sum(self, nim_board):
        val = 0
        bin_list = self.calculate_binary(nim_board)
        sum_list = [0, 0, 0]
        for i in range(len(bin_list)):
            for j in range(len(bin_list[i])):
                sum_list[j] += bin_list[i][j]
                
        
        for i in range(len(sum_list)):
            if sum_list[i] % 2 == 0:
                sum_list[i] = 0
            else:
                sum_list[i] = 1
        
        if sum_list == [0, 0, 0]:
            val = 1
        
        if sum_list[0] == 1:
            val = 5
        
        if sum_list[1] == 1:
            val = 3
            
        if sum_list[2] == 1:
            val = 2
            
        return val
    
    def nim_heuristic(self, nim_board):
        #Uses game strategy to calculate heuristic of every possible move in the given game state
        heur = 10
        one_rows = 0
        zero_rows = 0
        for i in range(len(nim_board)):
            heur = self.nim_sum(nim_board)
            if nim_board[i] == 1:
                one_rows += 1
            elif nim_board[i] == 0:
                zero_rows += 1
            if one_rows == 1 and zero_rows == len(nim_board) - 1:
                heur = 0
            elif one_rows == 3 and zero_rows == len(nim_board) - 3:
                heur = 0
            
            
            
        return heur
    
    def find_best_move(self, board_state):
        #Iterates through every possible move and returns the move with the lowest heuristic
        min_heiristic = 9
        
        for i in range(len(board_state)):
            if board_state[i] > 0:    
                for j in range(1, board_state[i] + 1, 1):
                    board_copy = board_state.copy()
                    board_copy[i] = board_copy[i] - j
                    if self.nim_heuristic(board_copy) < min_heiristic:
                        min_heiristic = self.nim_heuristic(board_copy)
                        
                        best_state = board_copy
        
        return best_state 
    
    def play(self, board_state):
        #Returns the best move for the given game state
        best_move = self.find_best_move(board_state)
        return best_move
    
    
nim_player = NimPlayer()

print(nim_player.play([1, 3, 5, 7]))


print(nim_player.play([1, 3, 5, 0]))


print(nim_player.play([1, 3, 0, 0]))


print(nim_player.play([0, 0, 4, 4]))

#printing out a few moves that the nim player would make given a game state




    
 
        