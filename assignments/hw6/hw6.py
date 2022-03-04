"""
Name: <Juyeoung Kim>
<hw6>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Juyeoung Kim>
"""
from math import pi

def cash_converter():

    """Write a function called cash_converter() that asks the user for an integer and prints the
    corresponding dollar value. Note that you must use the string method format()to produce the
    expected result. Use eval() to accept user input, do not use int()."""

    dollar_value = eval(input("enter an integer:"))
    print("$", '{:.2f}'.format(dollar_value))  # 소수점 몇번째 자리까지인지 외우자

def encode():

    #input
    message = input("enter the message to be encoded:")
    integer = eval(input("enter an integer key value:"))

    #convert
    for i in range(len(message)):
        code = message[i]
        uni_code = ord(code)
        new_code = uni_code + integer
        shifted_code = chr(new_code)

        print(shifted_code, end = "")


def sphere_area(radius):
    area = 4 * pi * radius ** 2
    return float(area)


def sphere_volume(radius):
    volume = 4 / 3 * pi * radius ** 3
    return float(volume)


def sum_n(number):
    acc = 0
    for i in range(1, number + 1):
        acc += i
    return int(acc)


def sum_n_cubes(number):
    acc = 0
    for i in range(1, number + 1):
        acc += i * i * i
    return int(acc)


def encode_better():
    pass



if __name__ == '__main__':
    cash_converter()
    encode()
    res = sphere_area(13)
    print(res)
    res = sphere_volume(13)
    print(res)
    res = sum_n(100)
    print(res)
    res = sum_n_cubes(13)
    print(res)
    encode_better()
