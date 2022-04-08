"""
Name: <Juyeoung Kim>
<hw10>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Juyeoung Kim>
"""


def fibonacci(n):
    n_1 = 1
    n_2 = 1
    count = 3

    if n < 1:
        return None
    elif n == 1 or n == 2:
        return 1

    while n >= count:
        next = n_1 + n_2
        n_1 = n_2
        n_2 = next
        count = count + 1

    return next


def double_investment(principle, rate):
    year = 0
    amount = 0
    double = 2 * principle

    while amount <= double:
        amount = principle * (1 + rate)
        year += 1
        principle = amount
    return year


def syracuse(n):
    n_list = []
    n_list.append(n)

    while n != 1:
        if n == 1:
            break

        elif n % 2 == 0:
            n = int(n / 2)
            n_list.append(n)

        else:
            n = 3 * n + 1
            n_list.append(n)

    return n_list

#
# def goldbach(n):
#     while

