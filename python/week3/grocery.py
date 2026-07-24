def main():
    groceries = {}

    while True:
        try:
            item = input().strip().upper()
            if item == "":
                continue

            if item in groceries:
                groceries[item] += 1
            else:
                groceries[item] = 1

        except EOFError:
            print()
            for item in sorted(groceries):
                print(groceries[item], item)
            break


main()