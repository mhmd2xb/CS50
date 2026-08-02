import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))?\s+(AM|PM)\s+to\s+(\d{1,2})(?::(\d{2}))?\s+(AM|PM)$"
    match = re.match(pattern, s.strip())

    if not match:
        raise ValueError("Invalid format")

    h1, m1, ap1, h2, m2, ap2 = match.groups()
    h1, h2 = int(h1), int(h2)
    m1 = int(m1) if m1 else 0
    m2 = int(m2) if m2 else 0

    if not (1 <= h1 <= 12) or not (1 <= h2 <= 12):
        raise ValueError("Invalid hour")
    if not (0 <= m1 <= 59) or not (0 <= m2 <= 59):
        raise ValueError("Invalid minute")

    h1 = h1 % 12 + (12 if ap1 == "PM" else 0)
    h2 = h2 % 12 + (12 if ap2 == "PM" else 0)

    return f"{h1:02d}:{m1:02d} to {h2:02d}:{m2:02d}"


if __name__ == "__main__":
    main()
