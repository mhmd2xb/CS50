"""Greeting value logic shared by week1 and week5."""


def value(greeting):
    """Return the amount owed for a greeting."""
    greeting = greeting.strip().lower()
    if greeting.startswith("hello"):
        return 0
    if greeting.startswith("h"):
        return 20
    return 100
