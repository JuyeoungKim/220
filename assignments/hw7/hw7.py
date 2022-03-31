"""
Name: <Juyeoung Kim>
<hw7>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
from encryption import encode, encode_better


def number_words(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    output = open(out_file_name, "w+")

    i = 1

    for line in infile:
        words = line.split()
        for word in words:
            output.write(str(i) + " " + word + "\n")
            i += 1



def hourly_wages(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    output = open(out_file_name, "w+")
    for line in infile:
        pats = line.split()
        wage = float(pats[2]) + 1.65

        wage = wage * int(pats[3])
        output.write(pats[0] + " " + pats[1] + " " + str(wage))



def calc_check_sum(isbn):
    acc = 0
    for i in range(10):
        pos = 10 - i
        acc += (pos * int(isbn[i]))
    return acc


def send_message(file_name, friend_name):
    infile = open(file_name, "r")
    outfile = open(friend_name + ".txt", "w+")
    for line in infile:
        outfile.write(line + "\n")


def encode(s,k):
    acc = ""
    for c in s:
        i = ord(c)
        key = k + i
        c = chr(key)
        acc += c
    return acc


def send_safe_message(file_name, friend_name, key):
    infile = open(file_name, "r")
    outfile = open(friend_name + ".txt", "w+")
    for line in infile:
        outfile.write(encode(line, key + "\n"))


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    padfile = open(pad_file_name, "r")
    key = padfile.read()
    infile = open(file_name, "r")
    outfile = open(friend_name + ".txt", "w+")
    for line in infile:
        outfile.write(encode_better(line, key))


def main():
    number_words("Walrus.txt", "Walrus_out.txt")
    hourly_wages("hourly_wages.txt", "hourly_wages_out.txt")
    print(calc_check_sum("0072946520"))
    send_message("message.txt", "dd")
    send_secret_message("secret_message.txt", "bob", 6)
    send_uncrackable_message("safest_message.txt", "Kylie", "pad.txt")

main()
