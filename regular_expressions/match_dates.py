import re

text = input()
pattern = r"(\d{2})([\.\-\/])([A-Z][a-z]{2})\2(\d{4})"
result = re.findall(pattern, text)
for date in result:
    print(f"Day: {date[0]}, Month: {date[2]}, Year: {date[3]}")
