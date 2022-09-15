"""EX04 - List Utils."""
__author__ = "730566282"

def all(input: list[int], integar: int) -> bool:
    i: int = 0
    while i < len(input):
        if integar == input[i]:
            i += 1
        else:
            return False
    return True

def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")