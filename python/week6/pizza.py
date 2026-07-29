import sys
import csv
from os.path import exists
from tabulate import tabulate


def main():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    if not filename.lower().endswith(".csv"):
        sys.exit("Not a csv file")

    if not exists(filename):
        sys.exit("File does not exist")

    try:
        with open(filename, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            rows = [[cell.strip() for cell in row] for row in reader]
    except Exception as e:
        sys.exit(f"Could not read file: {e}")

    print_grid(rows)


def print_grid(rows):

    try:
        if not rows:
            print("(no data)")
            return
        print(tabulate(rows, headers="firstrow", tablefmt="grid", stralign="left"))
    except Exception:

        if not rows:
            print("(no data)")
            return

        num_cols = max(len(r) for r in rows)
        padded = [r + [""] * (num_cols - len(r)) for r in rows]

        widths = [
            max(len(str(padded[r][c])) for r in range(len(padded)))
            for c in range(num_cols)
        ]

        def print_row(row):
            cells = [str(cell).ljust(widths[i]) for i, cell in enumerate(row)]
            print("| " + " | ".join(cells) + " |")

        sep = "+-" + "-+-".join("".ljust(w, "-") for w in widths) + "-+"

        print(sep)
        print_row(padded[0])
        print(sep)
        for row in padded[1:]:
            print_row(row)
        print(sep)


if __name__ == "__main__":
    main()
