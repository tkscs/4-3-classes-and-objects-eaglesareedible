import turtle as t
class Point:
    def __init__(self, x, y, label):
        self.x = x
        self.y = y
        self.label = label
    def __str__(self):
        return(f"({self.x}, {self.y}) {self.label}")
    def draw(self):
        print(self)
        t.goto(self.x, self.y)
        t.write(str(f"{self}"))
        t.dot()
    def scale(self, constant):
        x = self.x *constant
        y = self.y*constant
        label = self.label+".1"
        return Point(x, y, label)
    #def shear(self, xmul, ymul):
     #   self.x = self.x*xmul
     #   self.y = self.y*ymul
    #def shift(self, xshift=0, yshift=0):
     #   self.x+=xshift
      #  self.y+=yshift
    def add(self, nextpoint):
        x = self.x
        y = self.y
        label = self.label+"next"
        newpoint = Point(x, y, label)
    
#add a method to point class that adds another point to itself
goinglist = [(0, 0), (100, 0), (100, 100), (0, 100)]
point1 = Point(goinglist[0][0], goinglist[0][1], "Point 1")
point2 = Point(goinglist[1][0], goinglist[1][1], "Point 2")
point3 = Point(goinglist[2][0], goinglist[2][1], "Point 3")
point4 = Point(goinglist[3][0], goinglist[3][1], "Point 4")
#going.shear(9, 4)
#going2.shear(0, 2)
#going3.shear(5, 6)
#going4.shear(7, 7)

point1.draw()
point2.draw()
point3.draw()
point4.draw()

point2.draw()
scaledpoint2 =point2.scale(2)
scaledpoint2.draw()


t.exitonclick()