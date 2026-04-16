import turtle as t
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return(f"{self.x}, {self.y}")
    def draw(self):
        print(self)
        t.up()
        t.goto(self.x, self.y)
        t.down()
        t.write(str(self))
        t.dot()
goinglist = [(0, 0), (100, 0), (100, 100), (0, 100)]
going = Point(goinglist[0][0], goinglist[0][1])
going.draw()
going2 = Point(goinglist[1][0], goinglist[1][1])
going2.draw()
going3 = Point(goinglist[2][0], goinglist[2][1])
going3.draw()
going4 = Point(goinglist[3][0], goinglist[3][1])
going4.draw()
t.exitonclick()