from sys import argv, stdin
from string import ascii_lowercase, ascii_uppercase, \
    punctuation, whitespace, digits


def count_characters(string: str, char_set: set) -> int:
    """
    Count the number of characters in a string that are in a given set.

    Parameters:
        string (str): The string to be tested.
        char_set (set): The set to be used.

    Returns:
        int: The number of characters in the string that are in the set.
    """

    return sum(1 for character in string if character in char_set)


def print_character_counts(string: str) -> None:
    """
    Print the counts of different character types in the given string.

    Parameters:
        string (str): The string to be analyzed.
    """

    if not string:
        print("The text is empty.")
        return

    print(f"The text contains {len(string)} characters:")
    print(f"- {count_characters(string, ascii_uppercase)} upper letters")
    print(f"- {count_characters(string, ascii_lowercase)} lower letters")
    print(f"- {count_characters(string, punctuation)} punctuation marks")
    print(f"- {count_characters(string, whitespace)} spaces")
    print(f"- {count_characters(string, digits)} digits")


def main():
    """
    This program counts the number of different character types in a string.

    Parameters:
        argv[1] (str): The string to be analyzed.

    Returns:
        None
    """

    if len(argv) > 2:
        print("AssertionError: more than one argument is provided")
        return

    if len(argv) == 1 or not argv[1]:
        try:
            print("What is the text to count?")
            text = stdin.read()
        except KeyboardInterrupt:
            print("TRL+C was pressed")
            return

    else:
        text = argv[1]

    print_character_counts(text)


if __name__ == "__main__":
    main()
