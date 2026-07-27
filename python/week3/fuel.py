from shared.fuel import convert, gauge
from shared.prompts import prompt_until


def main():
    print(gauge(prompt_until("Fraction: ", convert)))


main()
