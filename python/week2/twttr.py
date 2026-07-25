text = input("enter your text: ").strip()
v = "aAeEiIoOuU"
for i in text :
    if i in v :
        text = text.replace(i,"")
print(text)