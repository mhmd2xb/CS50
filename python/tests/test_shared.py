import builtins

import pytest

from shared.bank import value
from shared.fuel import convert, gauge
from shared.plates import is_valid
from shared.prompts import iter_until_eof, prompt_int, prompt_until
from shared.text import camel_to_snake, remove_vowels


def fake_input(monkeypatch, answers):
    """Feed answers to input(), raising EOFError once they run out."""
    remaining = iter(answers)

    def _input(prompt=""):
        try:
            return next(remaining)
        except StopIteration:
            raise EOFError

    monkeypatch.setattr(builtins, "input", _input)


def test_prompt_until_skips_rejected_and_invalid_answers(monkeypatch):
    fake_input(monkeypatch, ["x", "-1", "7"])
    assert prompt_until("n: ", lambda a: int(a) if int(a) > 0 else None) == 7


def test_prompt_int_retries_until_valid(monkeypatch):
    fake_input(monkeypatch, ["nope", "0", "3"])
    assert prompt_int("Level: ", lambda level: level > 0) == 3


def test_iter_until_eof_strips_and_skips_blanks(monkeypatch):
    fake_input(monkeypatch, [" apple ", "", "pear"])
    assert list(iter_until_eof()) == ["apple", "pear"]


def test_remove_vowels():
    assert remove_vowels("Hello, World!") == "Hll, Wrld!"
    assert remove_vowels("AEIOU") == ""


def test_camel_to_snake():
    assert camel_to_snake("bestCoursesEver") == "best_courses_ever"
    assert camel_to_snake("Name") == "name"


def test_convert_and_gauge():
    assert convert("1/2") == 50
    assert gauge(0) == "E"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"


def test_convert_rejects_bad_fractions():
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ZeroDivisionError):
        convert("3/0")


def test_is_valid():
    assert is_valid("CS50")
    assert not is_valid("CS50P")
    assert not is_valid("CS05")


def test_value():
    assert value("Hello, World!") == 0
    assert value("Hey!") == 20
    assert value("What's up?") == 100
