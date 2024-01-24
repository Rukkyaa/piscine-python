import sys


def main():
    assert len(sys.argv) != 1, "no argument is provided"
    assert len(sys.argv) == 2, "more than one argument is provided"
    assert sys.argv[1].isdigit(), "argument is not an integer"

    number = int(sys.argv[1])
    print("I'm Even." if not number % 2 else "I'm Odd.")


if __name__ == "__main__":
    main()
