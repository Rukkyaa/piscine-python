from NULL_not_found import NULL_not_found


def main() -> None:
    """
    This program checks if the following data structures are NULL

    Parameters:
        None

    Returns:
        None
    """

    Nothing = None
    Garlic = float("NaN")
    Zero = 0
    Empty = ""
    Fake = False
    NULL_not_found(Nothing)
    NULL_not_found(Garlic)
    NULL_not_found(Zero)
    NULL_not_found(Empty)
    NULL_not_found(Fake)
    print(NULL_not_found("Brian"))


if __name__ == "__main__":
    main()
