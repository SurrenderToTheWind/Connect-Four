import pygame
import sys
import math

BOARD_SIZE = 10

from core import *

SCREEN_UPDATE = 30

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

BOARD_COLOR = (230, 230, 250)

FIELD_SIZE = 40

XMARGIN = int((WINDOW_WIDTH - BOARD_SIZE * FIELD_SIZE) / 2)
YMARGIN = int((WINDOW_HEIGHT - BOARD_SIZE * FIELD_SIZE) / 2)

YELLOW = 0
RED = 1
EMPTY = -1


class GUI:

    def calculate_column(self, x):
        return math.floor((x - XMARGIN) / FIELD_SIZE)

    def __init__(self, core):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.board = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.current_color = 0
        self.current_column = 0
        pygame.display.set_caption('Connect four')
        self.start_game(core, core.board_array)

    def start_game(self, core, board_list):
        while True:
            self.draw_board(board_list)
            pygame.display.flip()
            self.clock.tick()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = event.pos
                    x_max = WINDOW_WIDTH - XMARGIN
                    y_max = WINDOW_HEIGHT - YMARGIN
                    if x > XMARGIN and x < x_max and y < y_max:
                        self.current_column = self.calculate_column(x)
                        column = self.current_column
                        color = self.current_color
                        self.drop_pull(board_list, column, color, core)
                        free_row = self.get_empty_space_in_column(
                            column, core
                        )
                        if free_row is not -1:
                            column = self.current_column
                            board_list[column][free_row] = self.current_color
                            core.free_indexes_array[self.current_column] -= 1
                            self.draw_board(board_list)
                            pygame.display.flip()
                            if core.check_row_and_column_for_a_win(
                                self.current_column, free_row
                            ) or core.check_diagonals_for_a_win(
                                self.current_column, free_row
                            ):
                                winner_img = pygame.image.load('win.png')
                                rect_size = FIELD_SIZE * 3
                                winner_img = pygame.transform.smoothscale(
                                    winner_img, (rect_size, rect_size)
                                )
                                winner_rect1 = pygame.Rect(
                                    520, 180, rect_size, rect_size
                                )
                                winner_rect2 = pygame.Rect(
                                    0, 180, rect_size, rect_size
                                )
                                self.board.blit(winner_img, winner_rect1)
                                self.board.blit(winner_img, winner_rect2)
                                while True:
                                    pygame.display.flip()
                                    for event in pygame.event.get():
                                        if event.type is pygame.MOUSEBUTTONUP:
                                            pygame.quit()
                                            sys.exit()
                                        if event.type is pygame.QUIT:
                                            pygame.quit()
                                            sys.exit()
                            if (self.current_color == 0):
                                self.current_color = 1
                            else:
                                self.current_color = 0
                            pc_move = core.computer_move()
                            color = current_color
                            self.drop_pull(
                                board_list, pc_move[0], color, core
                            )
                            board_list[pc_move[0]][pc_move[1]] = color
                            core.free_indexes_array[pc_move[0]] -= 1
                            statement_1 = core.check_row_and_column_for_a_win(
                                pc_move[0], pc_move[1]
                            )
                            statement_2 = core.check_diagonals_for_a_win(
                                pc_move[0], pc_move[1]
                            )
                            if statement_1 or statement_2:
                                loser_img = pygame.image.load('loss.png')
                                loser_img = pygame.transform.smoothscale(
                                    loser_img, (FIELD_SIZE * 2, FIELD_SIZE * 1)
                                )
                                winner_rect1 = pygame.Rect(
                                    300, 0, FIELD_SIZE * 2, FIELD_SIZE * 1
                                )
                                winner_rect2 = pygame.Rect(
                                    300, 440, FIELD_SIZE * 2, FIELD_SIZE * 1
                                )
                                self.board.blit(loser_img, winner_rect1)
                                self.board.blit(loser_img, winner_rect2)
                                while True:
                                    pygame.display.flip()
                                    for event in pygame.event.get():
                                        if event.type is pygame.MOUSEBUTTONUP:
                                            pygame.quit()
                                            sys.exit()
                                        if event.type is pygame.QUIT:
                                            pygame.quit()
                                            sys.exit()
                            self.draw_board(board_list)
                            pygame.display.flip()
                            if (self.current_color == 0):
                                self.current_color = 1
                            else:
                                self.current_color = 0

    def draw_board(self, board_list, dropped_pull=None):
        self.board.fill(BOARD_COLOR)

        yellow_img = pygame.image.load('yellow_circle.png')
        yellow_img = pygame.transform.smoothscale(
            yellow_img, (FIELD_SIZE, FIELD_SIZE)
        )
        red_img = pygame.image.load('red_circle.png')
        red_img = pygame.transform.smoothscale(
            red_img, (FIELD_SIZE, FIELD_SIZE)
        )
        board_img = pygame.image.load('board_rect.png')
        board_img = pygame.transform.smoothscale(
            board_img, (FIELD_SIZE, FIELD_SIZE)
        )
        fields_rect = pygame.Rect(
            0, 0, FIELD_SIZE, FIELD_SIZE
        )

        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                fields_rect.topleft = (
                    XMARGIN + (x * FIELD_SIZE), YMARGIN + (y * FIELD_SIZE)
                )
                if board_list[x][y] == YELLOW:
                    self.board.blit(yellow_img, fields_rect)
                elif board_list[x][y] == RED:
                    self.board.blit(red_img, fields_rect)

        if dropped_pull is not None:
            if dropped_pull['color'] == RED:
                self.board.blit(
                    red_img, (dropped_pull['x'], dropped_pull['y'])
                )
            elif dropped_pull['color'] == YELLOW:
                self.board.blit(
                    yellow_img, (dropped_pull['x'], dropped_pull['y'])
                )

        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                fields_rect.topleft = (
                    XMARGIN + (x * FIELD_SIZE), YMARGIN + (y * FIELD_SIZE)
                )
                self.board.blit(board_img, fields_rect)

    def drop_pull(self, board_array, column, color, core):
        x = XMARGIN + column * FIELD_SIZE
        y = YMARGIN - FIELD_SIZE
        dropSpeed = 1.0

        empty_space = self.get_empty_space_in_column(column, core)

        while True:
            y += int(dropSpeed)
            dropSpeed += 0.5
            if int((y - YMARGIN) / FIELD_SIZE) >= empty_space:
                return
            self.draw_board(board_array, {'x': x, 'y': y, 'color': color})
            pygame.display.flip()
            self.clock.tick()

    # def get_empty_space_in_column(self, board_array, column):
    #     for y in range(BOARD_SIZE-1, -1, -1):
    #          if board_array[column][y] == EMPTY:
    #             return y
    #     return -1

    def get_empty_space_in_column(self, column, core):
        option = core.free_indexes_array[column]
        if option > -1:
            return core.free_indexes_array[column]
        else:
            return -1
