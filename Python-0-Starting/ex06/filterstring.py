from ft_filter import ft_filter
import sys


def main():
    """
Entry point of the program.
    """
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        sys.exit(1)

    string = sys.argv[1]
    try:
        number = int(sys.argv[2])
    except ValueError:
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    result = list(ft_filter(lambda x: len(x) > number, string.split()))

    print(result)


if __name__ == "__main__":
    main()
