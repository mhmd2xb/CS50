"""Fuel gauge logic shared by week3 and week5."""


def convert(fraction):
    """Convert an X/Y fraction into a percentage rounded to the nearest int."""
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    if x > y or x < 0 or y < 0:
        if y == 0:
            raise ZeroDivisionError
        raise ValueError

    return round(x / y * 100)


def gauge(percentage):
    """Render a percentage as E, F or "N%"."""
    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"
    return f"{percentage}%"
