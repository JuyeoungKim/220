"""
Name: <Juyeoung Kim>
<hw8>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Juyeoung Kim>
"""


def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sum_list(nums):
    acc = 0
    for i in range(len(nums)):
        acc += nums[i]
    return acc


def to_numbers(nums):
    for i in range(len(nums)):
        # Use eval() instead of float when you don't know if your input will be ints or floats
        nums[i] = eval(nums[i])


def sum_of_squares(nums):
    list_nums = nums.split()
    to_numbers(nums)
    square_each(nums)
    sum_list(nums)
    sum_list.append(nums)



def starter(weight, wins):
    # conditions
    if weight >= 150 and weight < 160 and wins >= 5:
        return True
    elif weight > 199 or wins > 20:
        return True

    return False


def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True

    return False


from graphics import *
import math


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    #first circle
    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    # Add a second circle
    center_two = win.getMouse()
    circumference_point_two = win.getMouse()
    radius_two = math.sqrt(
        (center_two.getX() - circumference_point_two.getX()) ** 2 + (center_two.getY() -
                                                                     circumference_point_two.getY()) ** 2)
    circle_two = Circle(center_two, radius_two)
    circle_two.setFill("Light green")
    circle_two.draw(win)


    win.getMouse()
    win.close()


def did_overlap(circle_one, circle_two):

    one_center = circle_one.getCenter()
    two_center = circle_two.getCenter()

    one_radius = circle_one.getRadius()
    two_radius = circle_two.getRadius()

    distance = math.sqrt((
        two_center.getX() - one_center.getX()) ** 2 + (two_center.getY() - one_center.getY()) ** 2)

    if distance <= one_radius + two_radius:
        return True
    else:
        return False


if __name__ == '__main__':
    # add_ten()
    # square_each()
    # sum_list()
    # starter()
    # leap_year()