import pytest

from meal import convert


def test_convert_whole_hours():
    assert convert("7:00") == 7.0
    assert convert("00:00") == 0.0


def test_convert_minutes():
    assert convert("7:30") == 7.5
    assert convert("12:15") == 12.25


def test_convert_end_of_day():
    assert convert("23:59") == pytest.approx(23.9833, abs=1e-4)


def test_convert_missing_minutes():
    with pytest.raises(ValueError):
        convert("7")


def test_convert_non_numeric():
    with pytest.raises(ValueError):
        convert("seven:oclock")
