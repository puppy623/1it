text = "Ahoj"
i = 0
for letter in text:
    print(letter, end= "-" if i < len(text) - 1 else "")
    i += 1
print()