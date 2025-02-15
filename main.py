from Window import Window, Line, Point

def main():
    win = Window(800,600)
    point1 = Point(100, 100)
    point2 = Point(50, 200)
    point3 = Point(150, 200)
    line1 = Line(point1, point2)
    line2 = Line(point2, point3)
    line3 = Line(point3, point1)

    win.draw_line(line1, "red")
    win.draw_line(line2, "red")
    win.draw_line(line3, "red")

    win.wait_for_close()

if __name__ == "__main__":
    main()
