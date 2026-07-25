import sys
import random
from pyfiglet import Figlet


def main():

    figlet = Figlet()

    if len(sys.argv) == 1:
        font = random.choice(figlet.getFonts())
        figlet.setFont(font=font)

    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):

        if sys.argv[2] not in figlet.getFonts():
            sys.exit("Invalid usage")

        figlet.setFont(font=sys.argv[2])

    else:
        sys.exit("Invalid usage")

    text = input("Input: ")
    print("Output:")
    print(figlet.renderText(text))


if __name__ == "__main__":
    main()