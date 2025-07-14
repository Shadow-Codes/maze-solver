from window import Line, Point, Window


def main():
    win = Window(800, 600)

    point_1 = Point(200, 300)
    point_2 = Point(600, 300)
    point_3 = Point(350, 200)
    point_4 = Point(100, 750)
    point_5 = Point(550, 200)
    point_6 = Point(300, 150)

    first_line = Line(point_1, point_2)
    second_line = Line(point_3, point_4)
    third_line = Line(point_5, point_6)

    win.draw_line(first_line, "red")
    win.draw_line(second_line, "black")
    win.draw_line(third_line, "red")

    win.wait_for_close()


if __name__ == "__main__":
    main()
