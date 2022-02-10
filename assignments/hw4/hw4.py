"""
Name: <Juyeoung Kim>
<hw4>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Juyeoung Kim>
"""

from graphics import *


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move circle")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(100, 50), Point(50, 100))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        click = win.getMouse()
        center = shape.getCenter()  # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()

        # Delete the shape.move(change_x, change_y) and add shape_2 to duplicate the shape
        shape_2 = shape.clone()
        shape_2.move(change_x, change_y)
        shape_2.draw(win)

    # print a message on the window “Click again to close” after the loop,
    # and wait for a final click before closing the window
    close_pt = Point(200, 200)
    close_instructions = Text(close_pt, "Click again to close")
    close_instructions.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    # Creates a graphical window
    width = 500
    height = 500
    win = GraphWin("Rectangle", width, height)

    # Two points of Rectangle
    click_1 = win.getMouse()
    point_1 = Point(click_1.getX(), click_1.getY())

    click_2 = win.getMouse()
    point_2 = Point(click_2.getX(), click_2.getY())

    # Draw a Rectangle and set the color
    shape = Rectangle(point_1, point_2)
    shape.setOutline("black")
    shape.setFill("green")
    shape.draw(win)

    # Click to close
    close_insructions = Text(Point(250, 250), "Click again to close")
    close_insructions.draw(win)

    # Calculate lines
    line_x = abs(click_1.getX() - click_2.getX())
    line_y = abs(click_1.getY() - click_2.getY())
    perimeter = 2 * (line_x + line_y)

    # Draw the perimeter
    perimeter_instructions = Text(Point(250, 450), "Perimeter: " + str(perimeter))
    perimeter_instructions.draw(win)

    # Draw the Area from lines
    area = (line_x * line_y)
    area_instructions = Text(Point(250, 475), "Area: " + str(area))
    area_instructions.draw(win)

    # Close the window by clicking
    win.getMouse()
    win.close()


import math


def circle():
    # Creates a graphing window
    width = 500
    height = 500
    win = GraphWin("Circle", width, height)

    # Center of the circle
    click_1 = win.getMouse()
    point_1 = Point(click_1.getX(), click_1.getY())

    # Second click
    click_2 = win.getMouse()
    point_2 = Point(click_2.getX(), click_2.getY())

    # Calculate the radius
    dx = (click_2.getX() - click_1.getX()) ** 2
    dy = (click_2.getY() - click_1.getY()) ** 2
    radius = math.sqrt(dx + dy)

    # Display radius
    radius_num_pt = Point(250, 450)
    radius_num = Text(radius_num_pt, "Radius: " + " " + str(radius))
    radius_num.draw(win)

    # Draw a circle
    circle_1 = Circle(point_1, radius)
    circle_1.draw(win)
    circle_1.setFill("blue")

    # closing instructions
    close_pt = Point(250, 250)
    close_instructions = Text(close_pt, "Click again to close")
    close_instructions.draw(win)

    # Close the window by clicking
    win.getMouse()
    win.close()

def pi2():

    acc = 0
    # the number of terms to sum
    terms_sum = eval(input("Enter the number of terms to sum:"))

    for i in range(terms_sum):

        plus_minus = -1 ** i
        num = 4
        denom = (2 * i) - 1
        total = acc + plus_minus * (num / denom)
        print(total)



if __name__ == '__main__':
    squares()
    rectangle()
    circle()
    pi2()