
import pygame
import random
import asyncio
import platform
from pygame.locals import *
from SudokuGenerator_RBT import *

#Initialize Pygame
pygame.init()

#Dimension, Fonts, and Constants
WIDTH, HEIGHT = 600, 700
CELL_SIZE = 60
GRID_SIZE = 9
BUTTON_HEIGHT = 50
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)

FONT = pygame.font.SysFont('arial', 36)
SMALL_FONT = pygame.font.SysFont('arial', 24)

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.sketched_value = 0
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.is_original = value != 0

    def set_cell_value(self, value):
        if not self.is_original:
            self.value = value
            self.sketched_value = 0

    def set_sketched_value(self, value):
        if not self.is_original:
            self.sketched_value = value

    def draw(self):
        x, y = self.col * CELL_SIZE, self.row * CELL_SIZE
        pygame.draw.rect(self.screen, WHITE, (x, y, CELL_SIZE, CELL_SIZE))
        if self.selected:
            pygame.draw.rect(self.screen, RED, (x, y, CELL_SIZE, CELL_SIZE))
        else:
            pygame.draw_rect(self.screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE))

        if self.value != 0:
            text = FONT.render(str(self.value), True, BLACK)
            self.screen.blit(text, (x + 20, y + 15))
        elif self.sketched_value != 0:
            text = SMALL_FONT.render(str(self.sketched_value), True, GRAY)
            self.screen.blit(text, (x + 5, y + 5))

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.selected_cell = None
        self.original_board = None
        self.generate_board()


    def generate_board(self):
        removed_cells = {'easy': 30, 'medium': 40, 'hard': 50}[self.difficulty]
        sudoku = generate_sudoku(GRID_SIZE, removed_cells)
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                self.cells[i][j] = Cell(sudoku[i][j], i, j, self.screen)
        self.original_board = [[self.cells[i][j].value for j in range(GRID_SIZE)] for i in range(GRID_SIZE)]

 #UNDER CONSTRUCTION
    # def draw(self):
    #
    #
    # def select(self):
    #
    #
    # def click(self, x, y):
    #
    #
    # def clear(self):
    #
    #
    # def sketch(self):
    #
    #
    # def place_number(self, value):
    #
    #
    # def reset_to_original(self):
    #
    #
    # def is_full(self):
    #
    #
    # def update_board(self):
    #
    #
    # def find_empty(self):
    #
    #
    # def check_board(self):
    #
