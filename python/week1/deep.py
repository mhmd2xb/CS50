text = input("Enter your input: ").strip().lower()
if text == "42":
    print("yes")
elif text == "forty-two":
    print("yes")
elif text == "forty two":
    print("yes")
else :
    print("no")