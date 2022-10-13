def ascii_characters(start, final):
    characters = []
    for char in range(ord(start) + 1, ord(final)):
        characters.append(chr(char))
    return " ".join(characters)


first = input()
second = input()
print(ascii_characters(first, second))
