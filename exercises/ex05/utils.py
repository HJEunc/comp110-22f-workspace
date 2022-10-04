"""EX05 - Utils."""
__author__ = "730566282"


def only_evens(xs: list[int]) -> list[int]:
    """Given a list of ints, return a new list containing only the elements of the input list that were even."""
    result: list[int] = []
    i: int = 0
    while i < len(xs):
        if (xs[i] % 2) == 0:
            result.append(xs[i])
        i += 1
    return result


def concat(xs: list[int], ys: list[int]) -> list[int]:
    """Given two lists of ints, combine to print one list."""
    result: list[int] = []
    i: int = 0
    while i < len(xs):
        result.append(xs[i])
        i += 1
    j: int = 0
    while j < len(ys):
        result.append(ys[j])
        j += 1
    return result


def sub(xs: list[int], start: int, end: int) -> list[int]:
    """Given a list, start index, and end index, return list values between them."""
    result: list[int] = []
    i: int = start
    if start < 0:
        i = 0
    if end > len(xs):
        end = len(xs)
    if xs == [] or start > end or end <= 0:
        return []
    while i < end:
        result.append(xs[i])
        i += 1
    return result