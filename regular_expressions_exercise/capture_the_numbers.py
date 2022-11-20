import re

pattern = r"\d+"
numbers = []
while True:
    string = input()
    if not string:
        break

    result = re.findall(pattern, string)
    if result:
        numbers.append(result)
for number in numbers:
    print(" ".join(number), end=" ")
