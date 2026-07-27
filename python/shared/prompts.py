"""Helpers for the input loops every problem set re-implements."""


def prompt_until(prompt, parse, errors=(ValueError,)):
    """Prompt until parse(answer) returns a value that is not None.

    Any exception listed in errors re-prompts instead of propagating.
    """
    while True:
        try:
            value = parse(input(prompt))
        except errors:
            continue
        if value is not None:
            return value


def prompt_int(prompt, is_valid=None):
    """Prompt until the answer is an integer accepted by is_valid."""

    def parse(answer):
        value = int(answer)
        if is_valid is None or is_valid(value):
            return value
        return None

    return prompt_until(prompt, parse)


def iter_until_eof(prompt=""):
    """Yield stripped, non-empty answers until the user sends EOF."""
    while True:
        try:
            line = input(prompt).strip()
        except EOFError:
            return
        if line:
            yield line
