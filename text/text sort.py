def accum(text):
    result = ""
    for znak in text:
        if result != "":
            result += "-" + znak.upper() + znak.lower() * text.index(znak)
        else:
            result += znak.upper() + znak.lower() * text.index(znak)
    return result
print(accum(input("Zadejte text: ")))
