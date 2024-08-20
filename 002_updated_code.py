# TODO: instead of taking a single string as argument,
# take a list of strings
# 002_updated_code.py (12-18)

def reverse_strings(strings):
    """
    Reverses a given list of strings.

    Args:
        strings (list[str]): The input list of strings.

    Returns:
        list[str]: The list of reversed strings.
    """
    return [s[::-1] for s in strings]

# Blank line here


print(reverse_strings(["uzma", "Sulthana",]))


def find_max(*args):
    """
    Finds the maximum of n numbers.

    Args:
        *args: Variable number of integers.

    Returns:
        int: The maximum number.

    Raises:
        TypeError: If any of the arguments are not integers.
    """
    if not all(isinstance(arg, int) for arg in args):
        raise TypeError("All arguments must be integers.")
    return max(args)


print(find_max(10, 20, 30))  # Output: 30
print(find_max(10, 30, 20))  # Output: 30
print(find_max(-10, -20, -30))  # Output: -10


def find_nth_largest(numbers, n):
    """
    Finds the nth largest number in a given list of numbers.

    Args:
        numbers (list): The list of numbers.
        n (int): The position of the number to find.

    Returns:
        int: The nth largest number.
        If there are less than n distinct numbers, returns None.
    """
    if n < 1 or n > len(set(numbers)):
        raise ValueError(
            "n must be between 1 and the number of distinct numbers")
    return sorted(set(numbers))[-n]


numbers = [4, 2, 9, 6, 5, 1, 8, 3, 7]
print(find_nth_largest(numbers, 1))  # 9
print(find_nth_largest(numbers, 2))  # 8
print(find_nth_largest(numbers, 3))  # 7
print(find_nth_largest(numbers, 4))  # 6
print(find_nth_largest(numbers, 5))  # 5
print(find_nth_largest(numbers, 6))  # 4
print(find_nth_largest(numbers, 7))  # 3
print(find_nth_largest(numbers, 8))  # 2
print(find_nth_largest(numbers, 9))  # 1
print(find_nth_largest(numbers, 10))  # None
