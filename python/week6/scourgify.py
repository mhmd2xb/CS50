import sys
from os.path import exists
from csv import DictReader, DictWriter
def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith(".csv"):
            sys.exit("Not a csv file")

    if not sys.argv[2].endswith(".csv"):
        sys.exit("Not a csv file")

    if not exists(filename):
        sys.exit(f"Could not read {filename}")


    with open(filename, "r", newline="") as f:
        reader = DictReader(f)
        students = []
        for row in reader:
            last, first = row["name"].split(', ')
            students.append({"first": first, "last": last, "house": row["house"]})
            
    with open(sys.argv[2], 'w') as result_file:
        writer = DictWriter(result_file, fieldnames=["first","last","house"])
        writer.writeheader()
        for row in students:
            writer.writerow(row)

         
if __name__ == "__main__":
    main()