def main() -> None:
    """
    This program prints the following data structures:
    - a list
    - a tuple
    - a set
    - a dictionary

    Parameters:
        None

    Returns:
        None
    """

    print(main.__doc__)
    ft_list = ["Hello", "World!"]
    ft_tuple = ("Hello", "France!")
    ft_set = {"Hello", "Paris!"}
    ft_dict = {"Hello": "42Paris!"}

    print(ft_list)
    print(ft_tuple)
    print(ft_set)
    print(ft_dict)


if __name__ == "__main__":
    main()
