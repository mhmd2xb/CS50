"""Small string transformations reused across problem sets."""

VOWELS = "aeiouAEIOU"


def remove_vowels(text):
    """Return text without any vowels."""
    return "".join(ch for ch in text if ch not in VOWELS)


def camel_to_snake(text):
    """Convert camelCase to snake_case."""
    snake = ""
    for ch in text:
        if ch.isupper():
            snake += "_" + ch.lower()
        else:
            snake += ch
    return snake.lstrip("_")
