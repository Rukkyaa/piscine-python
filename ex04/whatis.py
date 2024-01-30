from sys import argv


def main():
    if len(argv) == 1:
        return

    assert len(argv) == 2, "more than one argument is provided"

    try:
        number = int(argv[1])
        print("I'm Even." if not number % 2 else "I'm Odd.")
    except ValueError:
        raise AssertionError("argument is not an integer")


if __name__ == "__main__":
    main()
