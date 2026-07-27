import pytest

from tip import dollars_to_float, percent_to_float


def test_dollars_to_float():
    assert dollars_to_float("$50.00") == 50.00
    assert dollars_to_float("$0.00") == 0.00
    assert dollars_to_float("$1.23") == 1.23


def test_dollars_to_float_without_sign():
    assert dollars_to_float("12") == 12.0


def test_dollars_to_float_invalid():
    with pytest.raises(ValueError):
        dollars_to_float("$abc")


def test_percent_to_float():
    assert percent_to_float("15%") == 0.15
    assert percent_to_float("0%") == 0.0
    assert percent_to_float("100%") == 1.0


def test_percent_to_float_without_sign():
    assert percent_to_float("20") == 0.2


def test_percent_to_float_invalid():
    with pytest.raises(ValueError):
        percent_to_float("%")
