import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if match := re.search(r"^(0|[1-9]\d{0,2})\.(0|[1-9]\d{0,2})\.(0|[1-9]\d{0,2})\.(0|[1-9]\d{0,2})$", ip):
        octets = match.groups()
        if all(0 <= int(octet) <= 255 for octet in octets):
            return True
    return False


if __name__ == "__main__":
    main()