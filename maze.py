import random
import time

from cells import Cell
from window import Window


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

        if seed is not None:
            random.seed(seed)

    def __create_cells(self):
        for i in range(self.num_cols):
            self.__cells.append([])
            for j in range(self.num_rows):
                self.__cells[i].append(Cell(self.win))
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        x1_cell = self.x1 + (self.cell_size_x * i)
        y1_cell = self.y1 + (self.cell_size_y * j)
        x2_cell = x1_cell + self.cell_size_x
        y2_cell = y1_cell + self.cell_size_y

        self.__cells[i][j].draw(x1_cell, y1_cell, x2_cell, y2_cell)
        self.__animate()

    def __animate(self):
        if self.win:
            self.win.redraw()
        time.sleep(0.05)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[-1][-1].has_bottom_wall = False
        self.__draw_cell(self.num_cols - 1, self.num_rows - 1)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True

        while True:
            to_visit = []

            # cell check above
            if (
                0 <= i < self.num_cols
                and 0 <= j - 1 < self.num_rows
                and not self.__cells[i][j - 1].visited
            ):
                to_visit.append((i, j - 1))

            # cell check below
            if (
                0 <= i < self.num_cols
                and 0 <= j + 1 < self.num_rows
                and not self.__cells[i][j + 1].visited
            ):
                to_visit.append((i, j + 1))

            # cell check left
            if (
                0 <= i - 1 < self.num_cols
                and 0 <= j < self.num_rows
                and not self.__cells[i - 1][j].visited
            ):
                to_visit.append((i - 1, j))

            # cell check right
            if (
                0 <= i + 1 < self.num_cols
                and 0 <= j < self.num_rows
                and not self.__cells[i + 1][j].visited
            ):
                to_visit.append((i + 1, j))

            if to_visit == []:
                self.__draw_cell(i, j)
                return
            else:
                new_i, new_j = random.choice(to_visit)

                # new_cell = left
                if new_i < i and new_j == j:
                    self.__cells[i][j].has_left_wall = False
                    self.__cells[new_i][new_j].has_right_wall = False
                # new_cell = right
                if new_i > i and new_j == j:
                    self.__cells[i][j].has_right_wall = False
                    self.__cells[new_i][new_j].has_left_wall = False
                # new_cell = above
                if new_i == i and new_j < j:
                    self.__cells[i][j].has_top_wall = False
                    self.__cells[new_i][new_j].has_bottom_wall = False
                # new_cell = below
                if new_i == i and new_j > j:
                    self.__cells[i][j].has_bottom_wall = False
                    self.__cells[new_i][new_j].has_top_wall = False

            self.__break_walls_r(new_i, new_j)

    def __reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.__cells[i][j].visited = False

    def solve(self):
        return self.__solve_r(i=0, j=0)

    def __solve_r(self, i, j):
        self.__animate()
        self.__cells[i][j].visited = True

        if self.__cells[i][j] == self.__cells[self.num_cols - 1][self.num_rows - 1]:
            return True

        # cell check above
        if (
            0 <= i < self.num_cols
            and 0 <= j - 1 < self.num_rows
            and not self.__cells[i][j - 1].visited
            and not self.__cells[i][j].has_top_wall
            and not self.__cells[i][j - 1].has_bottom_wall
        ):
            self.__cells[i][j].draw_move(self.__cells[i][j - 1])
            if self.__solve_r(i, j - 1):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j - 1], True)

        # cell check below
        if (
            0 <= i < self.num_cols
            and 0 <= j + 1 < self.num_rows
            and not self.__cells[i][j + 1].visited
            and not self.__cells[i][j].has_bottom_wall
            and not self.__cells[i][j + 1].has_top_wall
        ):
            self.__cells[i][j].draw_move(self.__cells[i][j + 1])
            if self.__solve_r(i, j + 1):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j + 1], True)

        # cell check left
        if (
            0 <= i - 1 < self.num_cols
            and 0 <= j < self.num_rows
            and not self.__cells[i - 1][j].visited
            and not self.__cells[i][j].has_left_wall
            and not self.__cells[i - 1][j].has_right_wall
        ):
            self.__cells[i][j].draw_move(self.__cells[i - 1][j])
            if self.__solve_r(i - 1, j):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i - 1][j], True)

        # cell check right
        if (
            0 <= i + 1 < self.num_cols
            and 0 <= j < self.num_rows
            and not self.__cells[i + 1][j].visited
            and not self.__cells[i][j].has_right_wall
            and not self.__cells[i + 1][j].has_left_wall
        ):
            self.__cells[i][j].draw_move(self.__cells[i + 1][j])
            if self.__solve_r(i + 1, j):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i + 1][j], True)

        return False
