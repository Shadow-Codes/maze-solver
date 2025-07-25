import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._Maze__cells), num_cols)
        self.assertEqual(len(m1._Maze__cells[0]), num_rows)

    def test_maze_create_cells_symmetry(self):
        num_cols = 3
        num_rows = 3
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._Maze__cells), num_cols)
        for i in range(num_rows):
            self.assertEqual(len(m1._Maze__cells[i]), num_rows)

    def test_maze_create_cells_one_by_one(self):
        num_cols = 1
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._Maze__cells), num_cols)
        self.assertEqual(len(m1._Maze__cells[0]), num_rows)

    def test_break_entrance_and_exit(self):
        num_cols = 3
        num_rows = 3
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._Maze__break_entrance_and_exit()
        self.assertEqual(m1._Maze__cells[0][0].has_top_wall, False)
        self.assertEqual(
            m1._Maze__cells[num_rows - 1][num_cols - 1].has_bottom_wall, False
        )

    def test_visited_reset(self):
        num_cols = 6
        num_rows = 5

        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(m1._Maze__cells[0][0].visited, False)
        self.assertEqual(m1._Maze__cells[4][3].visited, False)
        self.assertEqual(m1._Maze__cells[num_cols - 1][num_rows - 1].visited, False)

    def test_visited_reset_manually(self):
        num_cols = 6
        num_rows = 5

        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        m1._Maze__cells[0][0].visited = True
        m1._Maze__cells[4][3].visited = True
        m1._Maze__cells[num_cols - 1][num_rows - 1].visited = True
        m1._Maze__reset_cells_visited()

        self.assertEqual(m1._Maze__cells[0][0].visited, False)
        self.assertEqual(m1._Maze__cells[4][3].visited, False)
        self.assertEqual(m1._Maze__cells[num_cols - 1][num_rows - 1].visited, False)


if __name__ == "__main__":
    unittest.main()
