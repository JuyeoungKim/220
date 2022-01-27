"""
Name: <Juyeoung Kim>
<hw2>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Juyeoung Kim>
"""
import math


def sum_of_threes():
    upper_bound = eval(input("what is the upper bound?"))
    sum = 0
    for i in range(0, upper_bound + 1, 3):
        sum = sum + i
    print(sum)



def multiplication_table():
    i = 1
    j = 1
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end = " ")
        print()



def triangle_area():
    a = eval(input("enter side a length:"))
    b = eval(input("enter side b length:"))
    c = eval(input("enter side c length:"))
    s = (a + b + c) / 2
    A = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(A)


def sum_squares():
    lower_range = eval(input("Enter lower range:"))
    upper_range = eval(input("Enter upper range:"))
    sum = 0
    for i in range(lower_range, upper_range + 1):
        sum = sum + (i ** 2)
    print(sum)


def power():
    base = eval(input("Enter base:"))
    exponent = eval(input("Enter exponent:"))
    power = base ** exponent
    print(power)



if __name__ == '__main__':
    sum_of_threes()
    multiplication_table()
    triangle_area()
    sum_squares()
    power()
