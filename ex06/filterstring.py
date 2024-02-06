from ft_filter import ft_filter
from sys import argv


def filter_string(string):
    """
    This function filters the given string based on the given length

    Parameters:
        string (str): string to filter
        length (int): length to filter

    Returns:
        bool: True if the string length is greater than the given length
    """

    return len(string) > int(argv[2])


def main():
    """
    This program filters the given string based on the given length

    Parameters:
        argv[1] (str): string to filter
        argv[2] (int): length to filter

    Returns:
        None
    """

    if len(argv) != 3:
        print("AssertionError: usage: filterstring.py \
<string-to-filter> <word-length>")
        return

    try:
        int(argv[2])
    except ValueError:
        print("AssertionError: argument is not an integer")
        return

    splitted_input = argv[1].split()
    min_length = int(argv[2])

    print(ft_filter(filter_string, splitted_input))
    print(ft_filter(lambda string: len(string) <= min_length, splitted_input))
    tab = ['Salut', 'ca', 'va', None, 'et', '',
           'toi', False, True, 'tu', 'vas', 0, 'bien', '', '?']
    print(ft_filter(None, tab))


if __name__ == "__main__":
    main()
