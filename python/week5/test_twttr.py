import twttr

def test_shorten():
    assert twttr.shorten("Hello, World!") == "Hll, Wrld!"
    assert twttr.shorten("AEIOU") == ""
    assert twttr.shorten("bcdfg") == "bcdfg"

def test_shorten_empty_string():
    assert twttr.shorten("") == ""

def test_shorten_numbers():
    assert twttr.shorten("12345") == "12345"
    assert twttr.shorten("A1E2I3O4U5") == "12345"

