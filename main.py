from Graphics import Window, Line, Point, Cell

def main():
    win = Window(800,600)
    
    cell1 = Cell(Point(50,50), Point(100,100), win)
    cell1.has_top_wall = False
    cell1.draw()

    cell2 = Cell(Point(100,50), Point(150,100), win)
    cell2.has_top_wall = False
    cell2.draw()

    cell3 = Cell(Point(50,100), Point(100,150), win)
    cell3.has_bottom_wall = False
    cell3.draw()

    cell4 = Cell(Point(100, 100), Point(150, 150), win)
    cell4.has_right_wall = False
    cell4.has_bottom_wall = False
    cell4.draw()

    win.wait_for_close()

if __name__ == "__main__":
    main()
