text = input("Enter your input: ").strip().lower()
if "hello" in text :
    print("$0")
elif text.startswith("h"):
    print("$20")
else:
    print("$100")