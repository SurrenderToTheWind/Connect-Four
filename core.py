from myProject1 import *

BOARD_SIZE = 10
FOUR = 4
EMPTY = -1


class Core:

    def __init__(self):
        self.board_array = [
            [-1 for i in range(0, BOARD_SIZE)] for x in range(0, BOARD_SIZE)
        ]
        self.free_indexes_array = [BOARD_SIZE-1 for x in range(0, BOARD_SIZE)]

    def get_empty_space_in_column(self, column):
        option = self.free_indexes_array[column]
        if option < 10:
            return self.free_indexes_array[column]
        else:
            return -1
        # for row in range(BOARD_SIZE-1, -1, -1):
        #      if self.board_array[row][column] == EMPTY:
        #         return row
        # return -1

    def check_row_and_column_for_a_win(self, column, row):
        color = self.board_array[column][row]

        start = column - 3
        if start < 0:
            start = 0
        end = column + 3
        if end > BOARD_SIZE - 1:
            end = BOARD_SIZE-1
        win = 1

        if end-start+1 < FOUR:
            return False

        while start < end:
            if self.board_array[start][row] == self.board_array[start+1][row]:
                if self.board_array[start][row] == color:
                    win += 1
                    if win >= FOUR:
                        return True
            else:
                win = 1
            start += 1

        start = row-3
        if start < 0:
            start = 0
        end = row + 3
        if end > BOARD_SIZE - 1:
            end = BOARD_SIZE - 1
        win = 1
        if end-start+1 < FOUR:
            return False

        while start < end:
            if self.board_array[column][start] == color:
                if self.board_array[column][start+1] == color:
                    win += 1
                    if win >= FOUR:
                        return True
            else:
                win = 1
            start += 1

        return False

    def check_diagonals_for_a_win(self, column, row):
        color = self.board_array[column][row]

        start = column - 3
        if start < 0:
            start = 0
        end = row + 3
        if end > BOARD_SIZE-1:
            end = BOARD_SIZE-1
        win = 1

        while start < BOARD_SIZE-1 and end > 0:
            if self.board_array[start][end] == color:
                if self.board_array[start+1][end-1] == color:
                    win += 1
                    if(win >= FOUR):
                        return True
            else:
                win = 1
            start += 1
            end -= 1

        start = column-3
        difference = abs(column - row)
        if start < 0:
            start = 0
        end = row - 3
        if end < 0:
            end = start + difference
            if end > BOARD_SIZE-1:
                end = BOARD_SIZE-1
        win = 1

        while start < BOARD_SIZE-1 and end < BOARD_SIZE-1:
            if self.board_array[start][end] == color:
                if self.board_array[start+1][end+1] == color:
                    win += 1
                    if(win >= FOUR):
                        return True
            else:
                win = 1
            start += 1
            end += 1

        return False

    def computer_move(self):
        # moves_array = [0 for x in range(0, BOARD_SIZE)]
        # self.best_moves(moves_array, 2)
        # best_move_index = 0
        # for move in range(0, len(moves_array)):
        #     print(move)
        #     if moves_array[move] > moves_array[best_move_index]:
        #         best_move_index = move
        # return (moves_array[best_move_index], best_move_index)

        for row in range(BOARD_SIZE-1, -1, -1):
            for col in range(0, BOARD_SIZE-1):
                if self.board_array[col][row] is -1:
                    return (col, row)
        return None


    # def best_moves(self, moves_array, depth):
    #     if depth is 0:
    #         return
    #     else:
    #         for column in range(0, BOARD_SIZE):
    #             row = self.free_indexes_array[column]
    #             print(column, row)
    #             if row < 0:
    #                 continue
    #             self.board_array[row][column] = 1
    #             self.free_indexes_array[column] -= 1
    #             if self.check_diagonals_for_a_win(row, column) or
    #self.check_row_and_column_for_a_win(row, column):
    #                 moves_array[column] += 1 * (depth+1)
    #             self.board_array[row][column] = 0
    #             if self.check_diagonals_for_a_win(row, column) or
    #self.check_row_and_column_for_a_win(row, column):
    #                     moves_array[column] += 1 * (depth + 1)
    #             else:
    #                 self.board_array[row][column] = 1
    #                 self.best_moves(moves_array, depth-1)
    #             self.board_array[row][column] = -1
    #             self.free_indexes_array[column] += 1

    # def alphabeta(self, column, row, depth, alpha, beta, player, help_array):
    #     if self.check_row_and_column_for_a_win(column, row) and
    #player == 1: #max
    #         return 20*(depth+1)
    #     elif self.check_diagonals_for_a_win(column, row)
    #and player == 1: #max
    #         return 20*(depth+1)
    #     elif self.check_row_and_column_for_a_win(column, row)
    #and player == 0: #min
    #         return -20*(depth+1)
    #     elif self.check_diagonals_for_a_win(column, row)
    #and player == 0: #min
    #         return -20*(depth+1)

    #     if depth == 0:
    #         return 0

    #     elif player is 1:
    #         for c in range(0, BOARD_SIZE-1):
    #             free_row = self.free_indexes_array[c]
    #             if help_array[free_row][c] == -1:
    #                 help_array[free_row][c] = player
    #                 self.free_indexes_array[c]-=1
    #                 alpha = max(
    #                    alpha, self.alphabeta(
    #                       free_row,c,depth-1,alpha, beta, 0, help_array))
    #                 help_array[free_row][c] = -1 #???
    #                 self.free_indexes_array[c]+=1 #???
    #             if beta<=alpha:
    #                 return alpha
    #         return alpha

    #     elif player is 0:
    #         for c in range(0, BOARD_SIZE-1):
    #             free_row = self.free_indexes_array[c]
    #             if help_array[free_row][c] == -1:
    #                 help_array[free_row][c] = player
    #                 self.free_indexes_array[c]-=1
    #                 beta = min(
    #                   alpha, self.alphabeta(
    #                       free_row,c,depth-1,alpha, beta, 0, help_array))
    #                 help_array[free_row][c] = -1
    #                 self.free_indexes_array[c]+=1 #???
    #             if beta<=alpha:
    #                 return beta
    #         return beta



# c2 = Core()
# c2.board_array =[
    #[1, 0, 1, 0, 1, 1, -1, 1, 4, 4],
    #[1, 0, 1, 0, 1, 1, -1, 1, 4, 4],
    #[1, 0, 1, 0, 4, 1, -1, 1, 4, 4],
    #[1, 0, 1, 0, 1, 1, 1, 1, 4, 4],
    #[1, 0, 1, 0, 1, 1, 1, 1, 4, 4],
    #[1, 0, 1, 0, 1, 1, 1, 1, 4, 4],
    #[1, 0, 1, 0, 4, 1, 1, 1, 1, 1],
    #[1, 0, 1, 0, 1, 1, 1, 1, 4, 4],
    #[1, 0, 1, 0, 1, 1, 1, 1, 4, 1],
    #[1, 0, 1, 0, 1, 1, 4, 4, 4, 4]
#]

# print(c2.get_empty_space_in_column(6))

# c1 = Core()
# c1.board_array = [
    # [-1,0,1,0,1,1,1,1,4,4]
    # [-1,0,1,0,1,1,1,1,4,4],
    # [-1,0,1,0,4,1,1,1,4,4],
    # [1,0,1,0,1,1,1,1,4,4],
    # [1,0,1,0,1,1,1,1,4,4],
    # [1,0,1,0,-1,1,1,1,4,4],
    # [1,0,1,0,4,1,1,1,1,4],
    # [1,0,1,0,1,1,1,1,4,4],
    # [1,0,1,0,1,1,1,1,4,4],
    # [1,0,1,0,1,1,4,4,4,4]
# ]

# # print(c1.get_empty_space_in_column(4))



# c = Core()
# c.board_array = [
# [1,0,1,0,1,1,1,1,4,4],
# [1,0,1,0,1,1,1,1,4,4],
# [1,0,1,0,4,1,1,1,4,4],
# [1,0,1,0,1,1,1,1,4,4],
# [1,0,1,0,1,1,1,1,4,4],
# [1,0,1,0,1,1,1,1,4,4],
# [1,0,1,0,4,1,1,1,1,4],
# [1,0,1,0,1,1,1,1,4,4],
# [1,0,1,0,1,1,1,1,4,4],
# [1,0,1,0,1,1,4,4,4,4]
# ]
# # if c.check_row_and_column_for_a_win(9,9):
# #     print("working")

# # if c.check_diagonals_for_a_win(9,9):
# #     print("working")
