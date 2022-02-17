"""
Name: <Juyeoung Kim>
<hw5>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Juyeoung Kim>
"""


# def name_reverse():
#     person_name = input("Enter a name (first last):")
#
#     # split the name
#     split_name = person_name.split()
#
#     # define the variables
#     first_name = split_name[0]
#     last_name = split_name[1]
#
#     # put them together to the order as I want and add the comma between these
#     reverse_name = last_name + ", " + first_name
#
#     print(reverse_name)


# def company_name():
#     domain_name = input("enter a three-part internet domain name:")
#     print(domain_name[4:-4])


# def initials():
#     input_number = eval(input("how many names will be input?"))
#     for i in range(input_number):
#         student_name = input("enter the names of the students in a class:")
#
#         # split the student name
#         ini_name = student_name.split()
#
#         first_split = ini_name[0]
#         last_split = ini_name[1]
#
#         # find the initials from each name
#         first_initial = first_split[0]
#         last_initial = last_split[0]
#
#         full_initial = first_initial + last_initial
#         print(full_initial)


def names():
    names_list = input("enter a list of names, first and last only, separated by commas:")
    names_split = names_list.split(",")
    names_length = len(names_split)

    for num in range(names_length):
        first_list = names_split[num]
        first_split = first_list.split(" ")
        first_length = len(first_split)

        for nums in range(first_length):
            second_split = first_split[nums]
            second_initial = second_split[0]


            print(second_initial, end=" ")









def thirds():
    pass


# def word_average():
#     # input a sentence and split it
#     sentence = input("Enter a sentence:")
#     sentence_split = sentence.split(" ")
#
#     # count the number of word
#     length_sentence = len(sentence_split)
#
#     # starting 0
#     acc = 0
#
#     # calculate the sum of the number of word by repeating as much as the number of word in sentence
#     for num in range(length_sentence):
#         num_word = len(sentence_split[num])
#         acc = acc + num_word
#
#     # calculate the average of the number of word and then print
#     average = acc / length_sentence
#     print(average)


# def pig_latin():
#
#     sentence = input("enter a sentence to convert to pig latin")
#
#     # split the sentence and count it
#     sentence_split = sentence.split()
#     length_sentence = len(sentence_split)
#
#     # move the first word to next to end of the word and add 'ay'
#     for num in range(length_sentence):
#         word = sentence_split[num]
#         first_word = word[0]
#         rest_word = word[1:]
#         full_word = rest_word + first_word
#         ay_word = full_word + 'ay'
#
#         print(ay_word, end=" ")


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    names()
    # thirds()
    # word_average()
    # pig_latin()