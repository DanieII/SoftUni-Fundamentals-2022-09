import re

string = input()
pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
result = re.findall(pattern, string)
print(" ".join(result))
