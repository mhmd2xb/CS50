from shared.prompts import prompt_until

MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def parse_date(raw_date):
    raw_date = raw_date.strip()

    if "/" in raw_date:
        month, day, year = raw_date.split("/")
    else:
        month, day, year = raw_date.split(" ")
        if "," not in day:
            return None
        day = day.replace(",", "")
        if month not in MONTHS:
            return None
        month = MONTHS.index(month) + 1

    day = int(day)
    month = int(month)

    if not 0 < day <= 31 or not 0 < month <= 12:
        return None

    return year, month, day


def main():
    year, month, day = prompt_until("Date: ", parse_date)
    print(f"{year}-{month:02}-{day:02}")


main()
