import sys
import os
from PIL import Image, ImageOps


def main():
    check_arguments()

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    shirt = load_shirt()
    image = load_image(input_file)

    result = resize_image(image, shirt)

    save_image(result, output_file)


def check_arguments():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_ext = get_extension(sys.argv[1])
    output_ext = get_extension(sys.argv[2])

    valid = [".jpg", ".jpeg", ".png"]

    if input_ext not in valid:
        sys.exit("Input does not exist")

    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")


get_extension = lambda filename: os.path.splitext(filename)[1].lower()

load_shirt = lambda: Image.open("shirt.png")

load_image = lambda filename: Image.open(filename)


def resize_image(image, shirt):
    image = ImageOps.fit(image, shirt.size)
    image.paste(shirt, (0, 0), shirt)
    return image


save_image = lambda image, filename: image.save(filename)


if __name__ == "__main__":
    main()