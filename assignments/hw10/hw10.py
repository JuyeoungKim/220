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
    if n == 1 or n == 2:
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
        # the function should stop once the amount has doubled
        if amount > double:
            return None
        amount = principle * (1 + rate)
        year += 1
        principle = amount
    return year


def syracuse(num):
    n_list = []
    n_list.append(num)

    while num != 1:
        if num == 1:
            break

        elif num % 2 == 0:
            num = int(num / 2)
            n_list.append(num)

        else:
            num = 3 * num + 1
            n_list.append(num)

    return n_list


def isprime(num):
    i = 2
    while i <= num / 2:
        if num % i == 0:
            return False
        i = i + 1
    return True

def goldbach(n):
    if n % 2 != 0:
        return
    i = 3
    j = n - 1
    while i < j:
        if isprime(i) == True and isprime(j) == True:
            if n == (i + j):
                return [i, j]
            elif n < (i + j):
                j = j - 1
            else:
                i = i + 1
        if isprime(i) == False:
            i = i + 1
        if isprime(j) == False:
            j = j - 1
    return
