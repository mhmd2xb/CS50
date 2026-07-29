import sys
from os.path import exists


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    if not exists(sys.argv[1]):
        sys.exit("File does not exist")

    filename = sys.argv[1]

    count = 0

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if line == "":
                continue

            if line.startswith("#"):
                continue

            count += 1

    print(count)

if __name__ == "__main__":
    main()
