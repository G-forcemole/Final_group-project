import random

class SudokuGenerator:
    """Constructor for the SudokuGenerator class.
	For the purposes of this project, row_length is always 9
	removed_cells could vary depending on the difficulty level chosen.
	"""
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for _ in range(row_length)]for _ in range(row_length)]
        self.fill_values()

    """Returns a 2D python list of numbers, which represents the board"""
    def get_board(self):
        return self.board

    """Displays the board to the console.
    	This is not strictly required, but it may be useful for debugging purposes.
    """
    def print_board(self):
          for row in self.board:
            print(row)

    """Returns a Boolean value.
    Determines if num is contained in the given row of the board."""
    def valid_in_row(self, row, num):
        return num not in self.board[row]

    """Returns a Boolean value.
    Determines if num is contained in the given column of the board."""
    def valid_in_col(self, col, num):
        return num not in [self.board[i][col]for i in range(self.row_length)]

    """Returns a Boolean value.  
    Determines if num is contained in the 3x3 box from 
    (row_start, col_start) to (row_start+2, col_start+2)"""
    def valid_in_box(self, row_start, col_start, num):
        for i in range(row_start, row_start + 3):
            for j in range(col_start + 3):
                if self.board[i][j] == num:
                    return False
        return True


    """Returns if it is valid to enter num at (row, col) in the board.
	This is done by checking the appropriate row, column, and box."""
    def is_valid(self, row, col, num):
        return(self.valid_in_row(row, num) and self.valid_in_col(col, num) and
               self.valid_in_box(row - row % 3, col - col % 3, num))


    """Randomly fills in values in the 3x3 box from 
    (row_start, col_start) to (row_start+2, col_start+2)."""
    def fill_box(self, row_start, col_start):
        numbers = list(range(1, 10))
        random.shuffle(numbers)
        idx = 0
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if idx < len(numbers):
                    self.board[i][j] = numbers[idx]
                    idx += 1


    """Fills the three boxes along the main diagonal of the board.
	This is the first major step in generating a Sudoku."""
    def fill_diagonal(self):
        for i in range(0, self.row_length, 3):
            self.fill_box(i, i)


    """This method is provided for students.
	Fills the remaining squares in the board.
	It is the second major step in generating a Sudoku.
	This will return a boolean."""
    def fill_remaining(self):
        #Placeholder for method provided by instructors
        pass


    """This method is provided for students.
	It constructs a solution by calling fill_diagonal and fill_remaining."""
    def fill_values(self):
        #Placeholder for method provided by instructors
        self.fill_diagonal()
        self.fill_remaining()


    """This method removes the appropriate number of cells from the board.
	It does so by randomly generating (row, col) coordinates of the board and 
    setting the value to 0.
    Note: Be careful not to remove the same cell multiple times. 
    A cell can only be removed once. 
    This method should be called after generating the Sudoku solution."""
    def remove_cells(self):
        cells_to_remove = self.removed_cells
        removed = set()
        while cells_to_remove > 0:
            row = random.randint(0, self.row_length - 1)
            col = random.randint(0, self.row_length - 1)
            if (row, col) not in removed and self.board[row][col] != 0:
                self.board[row][col] = 0
                removed.add((row, col))
                cells_to_remove -= 1


def generate_sudoku(size, removed):
    generator = SudokuGenerator(size, removed)
    generator.remove_cells()
    return generator.get_board()





