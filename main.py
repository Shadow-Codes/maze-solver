from cells import Cell
from maze import Maze
from window import Line, Point, Window


def main():
    win = Window(800, 600)
    maze_params = {
        "x1": 50,
        "y1": 50,
        "num_rows": 20,
        "num_cols": 30,
        "cell_size_x": 20,
        "cell_size_y": 20,
        "win": win,
    }

    maze_drawing = Maze(**maze_params)
    win.wait_for_close()


if __name__ == "__main__":
    main()
