import sys


def displays_sums_characters(string):
    # function that takes a string and displays the sum of its characters
    sum = 0
    for char in string:
        sum += 1
    print("The text contains", sum, "characters")


def displays_sums_lowercase(string):
    # function that takes a string and displays the sum of its lower-case
    sum = 0
    for char in string:
        if char.islower():
            sum += 1
    print(sum, "lower letters")


def displays_sums_uppercase(string):
    # function that takes a string and displays the sum of its upper-case
    sum = 0
    for char in string:
        if char.isupper():
            sum += 1
    print(sum, "upper letters")


def displays_sums_punctuation(string):
    # function that takes a string and displays the sum of its punctuation
    sum = 0
    for char in string:
        if char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
            sum += 1
    print(sum, "punctuation marks")


def displays_sums_spaces(string):
    # function that takes a string and displays the sum of its spaces
    sum = 0
    for char in string:
        if char.isspace():
            sum += 1
    print(sum, "spaces")


def displays_sums_digits(string):
    # function that takes a string and displays the sum of its digits
    sum = 0
    for char in string:
        if char.isdigit():
            sum += 1
    print(sum, "digits")


def main():
    # main fuction that take a single string and
    # displays the sums of its upper-case characters, lower-case
    # characters, punctuation characters, digits and spaces.

    # check if they are more than one argument
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return

    # check if the string is provided
    if len(sys.argv) == 1:
        # read the string from the user
        print("What is the text to count?")
        string = sys.stdin.read()
    else:
        # get the string from the command line
        string = sys.argv[1]

    # display the sum of characters
    displays_sums_characters(string)
    # display the sum of upper-case characters
    displays_sums_uppercase(string)
    # display the sum of lower-case characters
    displays_sums_lowercase(string)
    # display the sum of punctuation characters
    displays_sums_punctuation(string)
    # display the sum of spaces
    displays_sums_spaces(string)
    # display the sum of digits
    displays_sums_digits(string)


if __name__ == "__main__":
    main()
