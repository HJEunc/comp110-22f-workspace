"""Dictionary Utils Tests."""
__author__ = "730566282"


from exercises.ex07.dictionary import invert, favorite_color, count


# invert Tests:
def test_invert_one_dict() -> None:
    """Works with one dictionary."""
    given: dict[str, str] = {"hello": "goodbye"}
    assert invert(given) == {"goodbye": "hello"}


def test_invert_many_dicts() -> None:
    """Works with multiple dictionaries."""
    given: dict[str, str] = {"hello": "goodbye", "white": "black", "up": "down"}
    assert invert(given) == {"goodbye": "hello", "black": "white", "down": "up"}


def test_invert_empty_dict() -> None:
    """Works with empty dictionary."""
    given: dict[str, str] = {}
    assert invert(given) == {}


# favorite_color Tests:
def test_favorite_color_one_dict() -> None:
    """Works with one dictionary."""
    given: dict[str, str] = {"harrison": "blue"}
    assert favorite_color(given) == "blue"


def test_favorite_color_many_dicts() -> None:
    """Works with multiple dictionaries."""
    given: dict[str, str] = {"harrison": "blue", "alex": "yellow", "beck": "yellow"}
    assert favorite_color(given) == "yellow"


def test_favorite_color_empty_dict() -> None:
    """Works with empty dictionary."""
    given: dict[str, str] = {}
    assert favorite_color(given) == ""


# count Tests:
def test_count_one_item() -> None:
    """Works with one item."""
    given: list[str] = ["yes"]
    assert count(given) == {"yes": 1}


def test_count_many_item() -> None:
    """Works with multiple items."""
    given: list[str] = ["yes", "yes", "no"]
    assert count(given) == {"yes": 2, "no": 1}


def test_count_no_items() -> None:
    """Works with zero items."""
    given: list[str] = []
    assert count(given) == {}