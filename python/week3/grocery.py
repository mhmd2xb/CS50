from shared.prompts import iter_until_eof


def main():
    groceries = {}

    for item in iter_until_eof():
        item = item.upper()
        groceries[item] = groceries.get(item, 0) + 1

    print()
    for item in sorted(groceries):
        print(groceries[item], item)


main()
