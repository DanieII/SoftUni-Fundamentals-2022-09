import re

pattern = r"\b_([A-Za-z0-9]+)\b"
text = input()
result = re.findall(pattern, text)
print(",".join(result))
