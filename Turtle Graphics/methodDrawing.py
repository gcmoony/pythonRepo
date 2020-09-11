from turtle import Turtle, Screen
import random

"""
Time to destroy your CPU >:-)
"""

class Pen(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.default_width = 10
        self.offset = 0
        self.colors = ["red", "blue", "green", "black", "purple", "yellow"]

    def drawSpiralingBox(self, sizeOfBox):
        sizeOfBox = abs(sizeOfBox) * 2
        self.setheading(90)
        self.speed(0)
        self.goto(0, 0)
        #self.pencolor(random.choice(self.colors))
        # Draw Box
        self.fd(sizeOfBox)
        self.setheading(90 + self.offset)
        self.pd()
        self.fd(sizeOfBox)
        self.rt(90)
        self.fd(sizeOfBox * 2)
        self.rt(90)
        self.fd(sizeOfBox * 2)
        self.rt(90)
        self.fd(sizeOfBox)
        self.rt(90)
        self.fd(sizeOfBox)
        self.offset += 5
        self.up()

    def drawSpiralingBoxEdge(self, sizeOfBox):
        sizeOfBox = abs(sizeOfBox) * self.default_width
        self.setheading(90)
        self.speed(0)
        self.goto(0, 0)
        self.pencolor(random.choice(self.colors))
        # Draw Box
        self.fd(sizeOfBox)
        self.setheading(90 + self.offset)
        self.pd()
        self.fd(sizeOfBox)
        self.rt(90)
        self.fd(sizeOfBox * 2)
        self.rt(90)
        self.fd(sizeOfBox * 2)
        self.rt(90)
        self.fd(sizeOfBox * 2)
        self.rt(90)
        self.fd(sizeOfBox)
        self.offset += 5
        self.up()
        

    def drawSpiralBox(self, sizeOfBox):
        self.speed(0)
        sizeOfBox = abs(sizeOfBox) * self.default_width
        # Draw Box
        self.goto(-sizeOfBox, -sizeOfBox)
        self.setheading(90 + self.offset)
        self.pd()
        self.fd(sizeOfBox* 2)
        self.rt(90)
        self.fd(sizeOfBox * 2)
        self.rt(90)
        self.fd(sizeOfBox * 2)
        self.rt(90)
        self.fd(sizeOfBox * 2)
        self.setheading(90)
        self.offset += 10
        self.up()

    def drawBox(self, sizeOfBox):
        sizeOfBox = abs(sizeOfBox) * self.default_width
        current_widths = sizeOfBox
        # Draw Left Side
        self.goto(-current_widths, -current_widths)
        self.pd()
        self.goto(-current_widths, current_widths)

        # Draw Top
        self.goto(current_widths, current_widths)

        # Draw Right Side
        self.goto(current_widths, -current_widths)

        # Draw Bottom
        self.goto(-current_widths, -current_widths)
        self.up()

    def drawPositionalBox(self, value):
        self.goto(value * self.default_width, 0)
        sizeOfBox = abs(value) * self.default_width
        self.pd()
        # Draw Up
        self.seth(90)
        self.fd(sizeOfBox)
        # Draw Top
        self.seth(0)
        self.fd(self.default_width)
        self.seth(270)
        # Draw Down
        self.fd(sizeOfBox * 2)
        # Draw Bottom
        self.seth(180)
        self.fd(self.default_width)
        self.seth(90)
        # Close Side Line
        self.fd(sizeOfBox)
        self.up()


def main():
    # Initialize Turtle and Screen
    pen = Pen()
    paper = pen.getscreen()
    
    # Screen Settings
    screen_width = 250
    screen_height = 250
    paper.setworldcoordinates(-screen_width, -screen_height, screen_width, screen_height)

    # Turtle Settings
    pen.ht()
    pen.pensize(4)
    pen.up()
    
    
    # Get List of Variables
    val_List = []
    for value in range(-10, 10 + 1):
        val_List.append(value)

    while pen.offset <= 360:
        pen.drawSpiralingBox(36)
        

    #pen.clear()

    # Drawing Positional Values in an (X, Y) Plane
    #for item in val_List:
    #    pen.drawPositionalBox(item)
        #print(f"Moved to {item}")
        #pen.drawSpiralBox(item)
        #pen.drawBox(item)

    # Don't touch this    
    paper.exitonclick()

if __name__ == "__main__":
    main()