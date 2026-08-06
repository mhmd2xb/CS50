import sys
from datetime import date
import inflect


def get_birthdate():
    try:
        birth_input = input("Enter Date of birth: ")
        year, month, day = birth_input.strip().split("-")
        return date(int(year), int(month), int(day))
    except (ValueError, TypeError):
        sys.exit(1)


def number_to_words(n):
    p = inflect.engine()
    return p.number_to_words(n, andword="").capitalize()


def main():
    birthdate = get_birthdate()
    today = date.today()
    delta = today - birthdate
    minutes = delta.days * 24 * 60
    print(f"{number_to_words(minutes)} minutes")


if __name__ == "__main__":
    main()
