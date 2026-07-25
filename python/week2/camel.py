text = input("Enter camel Case: ")
text_snake_case = " "
for i in text:
    if i.isupper():
        text_snake_case += "_" + i.lower()
    else :
        text_snake_case +=  i
print(text_snake_case.lstrip('_'))