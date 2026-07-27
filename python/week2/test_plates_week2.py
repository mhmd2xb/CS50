from plates import is_valid


def test_valid_plates():
    assert is_valid("CS50") is True
    assert is_valid("AB") is True
    assert is_valid("AB1234") is True


def test_too_short_or_too_long():
    assert is_valid("A") is False
    assert is_valid("ABCDEFG") is False
    assert is_valid("") is False


def test_must_start_with_two_letters():
    assert is_valid("A1B") is False
    assert is_valid("1AB") is False


def test_digits_must_be_at_the_end():
    assert is_valid("CS50P") is False
    assert is_valid("AB1C") is False


def test_first_digit_cannot_be_zero():
    assert is_valid("CS05") is False
    assert is_valid("AA0") is False


def test_non_alphanumeric():
    assert is_valid("CS50!") is False
    assert is_valid("CS 50") is False
