from random import randint

def get_words(file_name):
    infile = open(file_name, "r")

    for line in infile:
        words = line.split()
        # print(words)
        return words


def get_random_word(words):
    random_word = randint(0, len(words)-1)
    choice_word = words[random_word]
    return choice_word


def letter_in_secret_word(letter, secret_word):
    """
    letter parameter is a single letter
    secret_word parameter is the chosen secret word for the game
    returns True if the letter is in the secret word, otherwise False
    """
    count = 0
    for i in secret_word:
        if i in letter:
            c += 1
    if c == len(letter):
        return True
    return False


def already_guessed(letter, guesses):
    s = []
    for i in letter:
        if i in guesses:
            s.append(i)

    ans = ""
    for i in letter:
        if i in s:
            ans += i
        ans += '_'
    return ans


def make_hidden_secret(secret_word, guesses):



def won(guessed):
    pass


def play_graphics(secret_word):
    pass


def play_command_line(secret_word):
    pass


if __name__ == '__main__':
    get_words("words.txt")
    get_random_word()
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)

main()