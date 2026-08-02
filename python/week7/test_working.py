from working import convert
import pytest


def test_valid_with_minutes():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 AM to 2:45 PM") == "10:30 to 14:45"


def test_valid_without_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 AM to 2 PM") == "10:00 to 14:00"


def test_midnight_and_noon():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"


def test_overnight():
    assert convert("9:00 PM to 5:00 AM") == "21:00 to 05:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"


def test_invalid_format():
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("9:00 to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to")
    with pytest.raises(ValueError):
        convert("9:00 XM to 5:00 PM")


def test_invalid_hour():
    with pytest.raises(ValueError):
        convert("25:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")


def test_invalid_minute():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:99 PM")
