"""EX05 - Utils Test."""
__author__ = "730566282"


from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


# only_evens tests
def test_only_evens_no_even() -> None:
    """Works without evens."""
    xs: list[int] = [1, 3, 5]
    assert only_evens(xs) == []


def test_only_evens_only_even() -> None:
    """Works with only evens."""
    xs: list[int] = [2, 4, 6]
    assert only_evens(xs) == [2, 4, 6]


def test_only_evens_empty() -> None:
    """Works if list is empty."""
    xs: list[int] = []
    assert only_evens(xs) == []


# concat tests
def test_concat_xs_empty() -> None:
    """Works if xs is empty."""
    xs: list[int] = []
    ys: list[int] = [2]
    assert concat(xs, ys) == [2]


def test_concat_ys_empty() -> None:
    """Works if ys is empty."""
    xs: list[int] = [5]
    ys: list[int] = []
    assert concat(xs, ys) == [5]


def test_concat_all_empty() -> None:
    """Works if both lists are empty."""
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []


def test_concat_all_full() -> None:
    """Works in normal condition."""
    xs: list[int] = [1, 2]
    ys: list[int] = [3, 4]
    assert concat(xs, ys) == [1, 2, 3, 4]


# sub tests
def test_sub_start_and_end() -> None:
    """Works if start and end are the true start and end indexes."""
    xs: list[int] = [1, 2, 3, 4, 5]
    start: int = 0
    end: int = 4
    assert sub(xs, start, end) == [1, 2, 3, 4]


def test_sub_out_of_range() -> None:
    """Works if start and end are out of range."""
    xs: list[int] = [1, 2, 3, 4, 5]
    start: int = -4
    end: int = 10
    assert sub(xs, start, end) == [1, 2, 3, 4, 5]


def test_sub_xs_empty() -> None:
    """Works if list is empty."""
    xs: list[int] = []
    start: int = 0
    end: int = 4
    assert sub(xs, start, end) == []