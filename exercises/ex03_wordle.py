"""EX03 - Structured Wordle."""

__author__ = "730566282"

def contains_char(searched_str: str, char_str: str) -> bool:
    """Search for a given character in a given string"""
    assert len(char_str) == 1
    i: int = 0
    while i < len(searched_str):
        if char_str[0] == searched_str[i]:
            return True
        else:
            i += 1
    return False