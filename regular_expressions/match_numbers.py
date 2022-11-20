import re

text = input()
# A valid number is a number that doesn't start with more than one 0
pattern = r"(^|(?<=\s))-?(0|[1-9][0-9]+)(\.\d+)?($|(?=\s))"
result = re.finditer(pattern, text)
for number in result:
    print(number.group(), end=" ")
