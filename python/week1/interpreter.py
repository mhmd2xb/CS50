import sys

try:
    x, y, z = input("enter your numbers: ").split(" ")
except ValueError:
    sys.exit("Invalid input: expected format 'number operator number'")

try:
    x = float(x)
    z = float(z)
except ValueError:
    sys.exit("Invalid input: operands must be numbers")

if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/":
    if z == 0:
        sys.exit("Invalid input: division by zero")
    print(x / z)
else:
    sys.exit(f"Invalid input: unknown operator {y!r}")
