import pytest
import fuel


def test_convert_correct():
    assert fuel.convert("1/2") == 50


def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("3/0")


def test_convert_value_error():
    with pytest.raises(ValueError):
        fuel.convert("2/1")


def test_convert_negative():
    with pytest.raises(ValueError):
        fuel.convert("-1/2")

    with pytest.raises(ValueError):
        fuel.convert("1/-2")


def test_gauge_empty():
    assert fuel.gauge(0) == "E"
    assert fuel.gauge(1) == "E"


def test_gauge_full():
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(100) == "F"


def test_gauge_percentage():
    assert fuel.gauge(25) == "25%"