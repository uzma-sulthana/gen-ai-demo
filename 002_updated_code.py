# TODO: instead of taking a single string as argument,
# take a list of strings
def reverse_string(s):
    """
    Reverses a given string.

    Args:
        s (str): The input string.

    Returns:
        str: The reversed string.
    """
    return s[::-1]


# TODO: update the function such that it can take n number
# of arguments and multiply them. then return the value
def find_max(a, b, c):
    """
    Finds the maximum of three numbers.

    Args:
        a (int): The first number.
        b (int): The second number.
        c (int): The third number.

    Returns:
        int: The maximum number.
    """
    return max(a, b, c)


# TODO: instead of just finding the second largest number,
# take an argument for nth largest number. check its less than
# the length of the number, if this condition passes, find the nth
# largest number
def find_second_largest(numbers):
    """
    Finds the second largest number in a given list of numbers.

    Args:
        numbers (list): The list of numbers.

    Returns:
        int: The second largest number.
        If there are less than two distinct numbers, returns None.
    """
    if len(set(numbers)) < 2:
        return None
    return sorted(set(numbers))[-2]
