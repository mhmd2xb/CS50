from random import randint

from shared.prompts import prompt_int


def main():
    number = randint(1, prompt_int("Level: ", lambda level: level > 0))

    while True:
        guess = prompt_int("Guess: ", lambda guess: guess > 0)

        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break


if __name__ == "__main__":
    main()
