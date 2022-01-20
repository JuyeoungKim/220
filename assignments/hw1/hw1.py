"""
Name: <Juyeoung Kim>
<hw1>.py

Problem: <This assignment need basic calculation and input method>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Juyeoung Kim>
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)
calc_rec_area()

def calc_volume():
    length = eval(input("Enter the length:"))
    width = eval(input("Enter the width:"))
    height = eval(input("Enter the height:"))
    volume = length * width * height
    print("Volume =", volume)
calc_volume()

def shooting_percentage():
    total_shots = eval(input("Enter the player's total shots:"))
    shots_made = eval(input("How many shots the player made?:"))
    shoot_per = ((shots_made / total_shots) * 100)
    print("Shooting percentage is:", shoot_per, "%")
shooting_percentage()


def coffee():
    coffee_amount = eval(input("How many pounds of coffee would you like?:"))
    coffee_cost = 10.50 * coffee_amount
    shipping_cost = 0.86 * coffee_amount
    fixed_cost = 1.5
    total_cost = coffee_cost + shipping_cost + fixed_cost
    print("You're total is:", "$", total_cost)
coffee()


def kilometers_to_miles():
    kilometers = eval(input("How many kilometers did you travel?:"))
    miles = kilometers / 1.61
    print("That's", miles, "miles!")
kilometers_to_miles()

if __name__ == '__main__':
    pass
