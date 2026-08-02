from um import count


def test_simple():
    assert count("um") == 1


def test_case_insensitive():
    assert count("Um") == 1
    assert count("UM") == 1
    assert count("uM") == 1


def test_multiple():
    assert count("um um um") == 3
    assert count("Um, UM, uM") == 3


def test_no_match():
    assert count("yummy") == 0
    assert count("humble") == 0
    assert count("album") == 0
    assert count("umfoo") == 0
    assert count("foum") == 0


def test_in_sentence():
    assert count("Hello, um, world") == 1
    assert count("um, yes, um, I think.") == 2
    assert count("Is this what you want? Um, yes!") == 1


def test_empty():
    assert count("") == 0


def test_only_um():
    assert count("um") == 1
    assert count("Um.") == 1
    assert count("Um,") == 1
    assert count("(um)") == 1
