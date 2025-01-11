import sys


def displays_sums_characters(string):
    """
    Calculate and display the total number of characters in a string.

    Parameters:
    string (str): The input string to analyze.

    Returns:
    None
    """
    sum = 0
    for char in string:
        sum += 1
    print("The text contains", sum, "characters")


def displays_sums_lowercase(string):
    """
    Calculate and display the total number of lowercase letters in a string.

    Parameters:
    string (str): The input string to analyze.

    Returns:
    None
    """
    sum = 0
    for char in string:
        if char.islower():
            sum += 1
    print(sum, "lower letters")


def displays_sums_uppercase(string):
    """
    Calculate and display the total number of uppercase letters in a string.

    Parameters:
    string (str): The input string to analyze.

    Returns:
    None
    """
    sum = 0
    for char in string:
        if char.isupper():
            sum += 1
    print(sum, "upper letters")


def displays_sums_punctuation(string):
    """
    Calculate and display the total number of punctuation marks in a string.

    Parameters:
    string (str): The input string to analyze.

    Returns:
    None
    """
    sum = 0
    for char in string:
        if char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
            sum += 1
    print(sum, "punctuation marks")


def displays_sums_spaces(string):
    """
    Calculate and display the total number of spaces in a string.

    Parameters:
    string (str): The input string to analyze.

    Returns:
    None
    """
    sum = 0
    for char in string:
        if char.isspace():
            sum += 1
    print(sum, "spaces")


def displays_sums_digits(string):
    """
    Calculate and display the total number of digits in a string.

    Parameters:
    string (str): The input string to analyze.

    Returns:
    None
    """
    sum = 0
    for char in string:
        if char.isdigit():
            sum += 1
    print(sum, "digits")


def main():
    """
    Main function to process a string and display various character counts.

    The function analyzes a string for the total count of characters, uppercase
    letters, lowercase letters, punctuation marks, spaces, and digits.

    Returns:
    None
    """
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return

    if len(sys.argv) == 1:
        print("What is the text to count?")
        string = sys.stdin.read()
    else:
        string = sys.argv[1]

    displays_sums_characters(string)
    displays_sums_uppercase(string)
    displays_sums_lowercase(string)
    displays_sums_punctuation(string)
    displays_sums_spaces(string)
    displays_sums_digits(string)


if __name__ == "__main__":
    main()
