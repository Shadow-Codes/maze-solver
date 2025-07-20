from cells import Cell
from maze import Maze
from window import Line, Point, Window


def main():
    screen_x_axis = 800
    screen_y_axis = 600

    win = Window(screen_x_axis, screen_y_axis)

    x1 = 50
    y1 = 50
    num_rows = 12
    num_cols = 16

    maze_params = {
        "x1": x1,
        "y1": y1,
        "num_rows": num_rows,
        "num_cols": num_cols,
        "cell_size_x": (screen_x_axis - 2 * x1) / num_cols,
        "cell_size_y": (screen_y_axis - 2 * y1) / num_rows,
        "win": win,
    }

    maze_drawing = Maze(**maze_params)
    maze_drawing.solve()
    win.wait_for_close()


if __name__ == "__main__":
    main()
