from time import time
from datetime import datetime


def main() -> None:
    """
    This program prints the number of seconds since January 1, 1970.
    It also prints the current date and time.

    Parameters:
        None

    Returns:
        None
    """

    total_seconds = time()
    formatted_seconds = "{:,}".format(total_seconds)

    formatted_time = datetime.now().strftime("%b %d %Y")

    print(f"Seconds since January 1, 1970: {formatted_seconds} or \
{total_seconds:.2e} in scientific notation", formatted_time, sep="\n")


if __name__ == "__main__":
    main()
