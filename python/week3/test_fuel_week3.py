import pytest

import fuel


def test_convert_fraction():
    assert fuel.convert("1/2") == 0.5
    assert fuel.convert("3/4") == 0.75
    assert fuel.convert("0/5") == 0.0


def test_convert_numerator_greater_than_denominator():
    with pytest.raises(ValueError):
        fuel.convert("3/2")


def test_convert_negative():
    with pytest.raises(ValueError):
        fuel.convert("-1/2")


def test_convert_non_integer():
    with pytest.raises(ValueError):
        fuel.convert("one/two")


def test_convert_missing_slash():
    with pytest.raises(ValueError):
        fuel.convert("12")


def test_gauge_empty():
    assert fuel.gauge(0) == "E"
    assert fuel.gauge(0.01) == "E"


def test_gauge_full():
    assert fuel.gauge(1) == "F"
    assert fuel.gauge(0.99) == "F"


def test_gauge_percentage():
    assert fuel.gauge(0.25) == "25%"
    assert fuel.gauge(0.5) == "50%"
