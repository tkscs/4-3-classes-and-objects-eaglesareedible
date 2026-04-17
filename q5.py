import turtle as t
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return(f"{self.x}, {self.y}")
    def __repr__(self):
        return(f"{self.x}, {self.y}")
    def draw(self):
        print(self)
        t.goto(self.x, self.y)
        t.write(str(self))
        t.dot()
    def shear(self, xmul, ymul):
        self.x = self.x*xmul
        self.y = self.y*ymul
    def shift(self, xshift=0, yshift=0):
        self.x+=xshift
        self.y+=yshift
    
#add a method to point class that adds another point to itself
goinglist = [(0, 0), (100, 0), (100, 100), (0, 100)]
going = Point(goinglist[0][0], goinglist[0][1])
going2 = Point(goinglist[1][0], goinglist[1][1])
going3 = Point(goinglist[2][0], goinglist[2][1])
going4 = Point(goinglist[3][0], goinglist[3][1])
going.shear(9, 4)
going2.shear(0, 2)
going3.shear(5, 6)
going4.shear(7, 7)

going.draw()
going2.draw()
going3.draw()
going4.draw()




t.exitonclick()