def main():
    text = input("enter your text: ").strip()
    print(shorten(text))

def shorten(text):
    v = "aAeEiIoOuU"
    for i in text:
        if i in v:
            text = text.replace(i, "")
    return text