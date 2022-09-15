"""EX04 - List Utils."""
__author__ = "730566282"

def all(input: list[int], integar: int) -> bool:
    """Given a list of ints and an int, return bool indicating
    if all int values in list are the same as given int."""
    i: int = 0
    while i < len(input):
        if integar == input[i]:
            i += 1
        else:
            return False
    return True

def max(input: list[int]) -> int:
    """Given a list of ints, returns largest int."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max: int = input[0]
    i: int = 1
    while i < len(input):
        if input[i] < max:
            i += 1
        else:
            max = input[i]
            i += 1
    return max

def is_equal(input1: list[int], input2: list[int]) -> bool:
    """Given two lists of ints, returns bool indicating whether they are equal."""
    if len(input1) != len(input2):
        return False
    i: int = 0
    while i < len(input1):
        if input1[i] == input2[i]:
            i += 1
        else:
            return False
    return True