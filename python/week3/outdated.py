months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

while True:
    raw_date = input("Date: ").strip()
    if '/' in raw_date:
        month, day, year = raw_date.split('/')

    else:
        month, day, year = raw_date.split(' ')
        if ',' not in day:
            continue

        day = day.replace(',', '')
        try:
            month = months[month]
        except KeyError:
            continue

    try:
        day = int(day)
        month = int(month)
    except ValueError:
        continue

    if not 0 < day <= 31 or not 0 < month <= 12:
        continue

    break

print(f"{year}-{month:02}-{day:02}")