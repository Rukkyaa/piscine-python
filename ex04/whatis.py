from sys import argv


def main():
    """
    This program checks if the given number is even or odd

    Parameters:
        argv[1] (int): number to check

    Returns:
        None
    """

    if len(argv) == 1:
        return

    if len(argv) != 2:
        print("AssertionError: more than one argument is provided")
        return

    try:
        number = int(argv[1])
        print("I'm Even." if not number % 2 else "I'm Odd.")
    except ValueError:
        print("AssertionError: argument is not an integer")
        return


if __name__ == "__main__":
    main()
