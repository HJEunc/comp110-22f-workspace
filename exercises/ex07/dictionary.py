"""EX07 - Dictionary Utils."""
__author__ = "730566282"


def invert(given: dict[str, str]) -> dict[str, str]:
    """Inverts the key and value in a dictinary."""
    result: dict[str, str] = {}
    for key in given:
        if given[key] in result:
            raise KeyError
        result[given[key]] = key
    return result


def favorite_color(given: dict[str, str]) -> str:
    """Returns the value that shows up the most in a dictionary."""
    last_counter: int = 0
    largest: str = ""
    for key in given:
        counter: int = 0
        current_key: str = key
        for key in given:
            if key == current_key:
                counter += 1
        if last_counter < counter:
            last_counter: int = counter
            largest = given[key]
        else:
            counter = 0
    return largest

        
def count(given: list[str]) -> dict[str, int]:
    """Returns a dictionary that counts how much each unique item appears in a list."""
    result: dict[str, int] = {}
    for item in given:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result