from shared.plates import is_valid


def main():
    plate = input("Plate: ")
    print("Valid" if is_valid(plate) else "Invalid")


if __name__ == "__main__":
    main()
