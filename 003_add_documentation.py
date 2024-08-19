def reverse_string(s):
    return s[::-1]


def find_max(a, b, c):
    return max(a, b, c)


def find_second_largest(numbers):
    if len(set(numbers)) < 2:
        return None
    return sorted(set(numbers))[-2]
