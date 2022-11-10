string = input()
digits, letters, other = [], [], []
for element in string:
    if element.isdigit():
        digits.append(element)
    elif element.isalpha():
        letters.append(element)
    else:
        other.append(element)
print(*digits, sep="")
print(*letters, sep="")
print(*other, sep="")
