"""Vanity plate validation shared by week2 and week5."""


def is_valid(s):
    """Return True when s is a valid vanity plate."""
    if not 2 <= len(s) <= 6:
        return False
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    if not s.isalnum():
        return False

    for i, ch in enumerate(s):
        if ch.isdigit():
            return ch != "0" and s[i:].isdigit()

    return True
