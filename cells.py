from window import Line, Point, Window


class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        left_wall = Line(Point(x1, y1), Point(x1, y2))
        right_wall = Line(Point(x2, y1), Point(x2, y2))
        top_wall = Line(Point(x1, y1), Point(x2, y1))
        bottom_wall = Line(Point(x2, y2), Point(x1, y2))

        if self.has_left_wall:
            self.__win.draw_line(left_wall)
        if self.has_right_wall:
            self.__win.draw_line(right_wall)
        if self.has_top_wall:
            self.__win.draw_line(top_wall)
        if self.has_bottom_wall:
            self.__win.draw_line(bottom_wall)

    def calculate_center(self):
        x = (self.__x1 + self.__x2) / 2
        y = (self.__y1 + self.__y2) / 2

        return (x, y)

    def draw_move(self, to_cell, undo=False):
        if not undo:
            color = "red"
        else:
            color = "gray"

        line_startpoint = self.calculate_center()
        line_endpoint = to_cell.calculate_center()
        line = Line(
            Point(line_startpoint[0], line_startpoint[1]),
            Point(line_endpoint[0], line_endpoint[1]),
        )
        self.__win.draw_line(line, color)
