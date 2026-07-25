def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if 2 <= len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha():
            if s.isalnum():
                found_digit = False
                for i, ch in enumerate(s):
                    if ch.isdigit():
                        found_digit = True
                        if ch == "0":
                            return False
                        elif s[i:].isdigit():
                            return True
                        else:
                            return False
                if not found_digit:
                    return True
    return False

main()