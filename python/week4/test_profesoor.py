import builtins

import pytest

from profesoor import generate_integer, get_level


@pytest.mark.parametrize(
    "level, low, high",
    [(1, 0, 9), (2, 10, 99), (3, 100, 999)],
)
def test_generate_integer_range(level, low, high):
    for _ in range(100):
        assert low <= generate_integer(level) <= high


def test_get_level_accepts_valid_level(monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda *_: "2")
    assert get_level() == 2


def test_get_level_retries_until_valid(monkeypatch):
    answers = iter(["0", "abc", "4", "3"])
    monkeypatch.setattr(builtins, "input", lambda *_: next(answers))
    assert get_level() == 3
