"""
Name: <Juyeoung Kim>
<hw3>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Juyeoung Kim>
"""


def average():
    number = eval(input("How many grades will you enter?:"))
    acc = 0
    for i in range(number):
        grades = eval(input("enter grade:"))
        acc = acc + grades
    ave = acc / number
    print(ave)


def tip_jar():
    acc = 0
    for i in range(5):
        i = eval(input("How much would you like to donate?"))
        acc = acc + i
    print("total tips:", acc)


def newton():
    roots = eval(input("what number do you want square root?"))
    times = eval(input("How many times should we improve the approximation?"))
    approx = roots / 2

    for i in range(times):
        approx = (approx + (roots / approx)) / 2
    print("the square root is approximately", approx)


def sequence():
    terms = eval(input('how many terms would you like?'))
    for i in range(terms):
        i = 1 + (i // 2 * 2)
        print(i, end = " ")


def pi():
    acc = 1
    series = eval(input('how many terms in the series?'))
    for i in range(series):
        numerater = 2 + (i // 2 * 2)
        denumerator = 1 + ((i + 1) // 2 * 2)
        acc = acc * (numerater / denumerator)

    print(acc * 2)


if __name__ == '__main__':
    average()
    tip_jar()
    newton()
    sequence()
    pi()

