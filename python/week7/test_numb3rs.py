from numb3rs import validate


def test_valid_addresses():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("192.168.1.1") == True
    assert validate("10.0.0.1") == True
    assert validate("127.0.0.1") == True
    assert validate("1.1.1.1") == True


def test_invalid_octets():
    assert validate("256.0.0.0") == False
    assert validate("0.256.0.0") == False
    assert validate("0.0.256.0") == False
    assert validate("0.0.0.256") == False
    assert validate("999.999.999.999") == False


def test_invalid_format():
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False
    assert validate("1.2.3.") == False
    assert validate(".1.2.3.4") == False
    assert validate("1..2.3") == False


def test_letters():
    assert validate("abc.def.ghi.jkl") == False
    assert validate("a.b.c.d") == False


def test_negative_and_special():
    assert validate("-1.0.0.0") == False
    assert validate("1.2.3.-1") == False
    assert validate("1.2.3.4 ") == False
    assert validate(" 1.2.3.4") == False
