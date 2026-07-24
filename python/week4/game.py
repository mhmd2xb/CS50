from random import randint

def main():
    while True:
        try:
            num = int(input("Level: "))
            if num <= 0:
                continue
            break
        except ValueError:
            pass

    number = randint(1, num)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                continue
        except ValueError:
            continue

        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break


if __name__ == "__main__":
    main()