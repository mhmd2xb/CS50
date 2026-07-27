from faces import convert


def test_convert_happy():
    assert convert("Hello :)") == "Hello 🙂"
    assert convert("Hello :(") == "Hello 🙁"


def test_convert_both_faces():
    assert convert(":):(") == "🙂🙁"


def test_convert_repeated():
    assert convert(":) :) :)") == "🙂 🙂 🙂"


def test_convert_no_faces():
    assert convert("") == ""
    assert convert("no emoticons here") == "no emoticons here"
    assert convert(":-)") == ":-)"
