import random


def main():
    score = 0
    level = get_level()

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        for attempt in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                if attempt == 2:
                    print(f"{x} + {y} = {x + y}")
                continue

            if answer == x + y:
                score += 1
                break

            print("EEE")

            if attempt == 2:
                print(f"{x} + {y} = {x + y}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()