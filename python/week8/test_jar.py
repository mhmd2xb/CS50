import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar2 = Jar(20)
    assert jar2.capacity == 20
    assert jar2.size == 0

    with pytest.raises(ValueError):
        Jar(-1)

    with pytest.raises(ValueError):
        Jar("abc")

    with pytest.raises(ValueError):
        Jar(3.14)


def test_str():
    jar = Jar()

    assert str(jar) == ""

    jar.deposit(3)
    assert str(jar) == "\U0001f36a" * 3

    jar.deposit(2)
    assert str(jar) == "\U0001f36a" * 5

    jar.withdraw(1)
    assert str(jar) == "\U0001f36a" * 4


def test_deposit():
    jar = Jar()

    jar.deposit(3)
    assert jar.size == 3

    jar.deposit(2)
    assert jar.size == 5

    jar2 = Jar(3)
    jar2.deposit(3)
    assert jar2.size == 3

    with pytest.raises(ValueError):
        jar2.deposit(1)

    with pytest.raises(ValueError):
        jar.deposit(-1)

    with pytest.raises(ValueError):
        jar.deposit("abc")


def test_withdraw():
    jar = Jar()
    jar.deposit(5)

    jar.withdraw(2)
    assert jar.size == 3

    jar.withdraw(3)
    assert jar.size == 0

    jar.deposit(2)
    with pytest.raises(ValueError):
        jar.withdraw(5)

    with pytest.raises(ValueError):
        jar.withdraw(-1)

    with pytest.raises(ValueError):
        jar.withdraw("abc")
