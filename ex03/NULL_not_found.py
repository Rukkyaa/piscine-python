def NULL_not_found(object: any) -> int:
    """
    This function is used to print the type of the object if it is a null type.
    Otherwise, it will print that the object is not a null type.

    Parameters:
        object (any): The object to be tested.

    Returns:
        int: 0 if object is a null type, 1 otherwise.
    """

    null_types = [None, 0, "", False]

    if object in null_types or str(object) == "nan":
        print(object.__class__)
        return 0

    print(f"{object.__class__} is not a null type")
    return 1
