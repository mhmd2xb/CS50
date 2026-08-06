import pytest
from datetime import date
from seasons import get_birthdate, number_to_words


def test_get_birthdate_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2005-03-24")
    result = get_birthdate()
    assert result == date(2005, 3, 24)


def test_get_birthdate_invalid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "invalid")
    with pytest.raises(SystemExit):
        get_birthdate()


def test_get_birthdate_wrong_format(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "24-03-2005")
    with pytest.raises(SystemExit):
        get_birthdate()


def test_get_birthdate_empty(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "")
    with pytest.raises(SystemExit):
        get_birthdate()


def test_number_to_words_small():
    assert number_to_words(1) == "One"
    assert number_to_words(15) == "Fifteen"
    assert number_to_words(50) == "Fifty"
    assert number_to_words(99) == "Ninety-nine"


def test_number_to_words_hundreds():
    assert number_to_words(100) == "One hundred"
    assert number_to_words(150) == "One hundred fifty"
    assert number_to_words(999) == "Nine hundred ninety-nine"


def test_number_to_words_thousands():
    assert number_to_words(1000) == "One thousand"
    assert number_to_words(1500) == "One thousand, five hundred"
    assert number_to_words(525600) == "Five hundred twenty-five thousand, six hundred"


def test_number_to_words_millions():
    assert number_to_words(1_000_000) == "One million"
    assert number_to_words(11_239_200) == "Eleven million, two hundred thirty-nine thousand, two hundred"


def test_number_to_words_commas():
    result = number_to_words(11_239_200)
    assert "," in result
    assert "million," in result
    assert "thousand," in result


def test_number_to_words_zero():
    assert number_to_words(0) == "Zero"
