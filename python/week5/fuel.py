def main():
    while True:
        try:
            fraction = input("Fraction: ")
            fuel = convert(fraction)
            print(gauge(fuel))
            break
        except ValueError:
            pass


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    if  x > y or x < 0 or y < 0:
        if y == 0:
            raise ZeroDivisionError
        raise ValueError
    return round(x/y * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
