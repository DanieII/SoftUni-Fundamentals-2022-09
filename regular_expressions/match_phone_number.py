import re

text = input()
# back reference patterns
# The boundary is set because the string should end with the fourth number
# r"(\+359)(\s|\-)2\2(\d{3})\2(\d{4})\b"
# r"(\+359)([\-\s])2\2(\d{3})\2(\d{4})\b"

# Easier pattern
pattern = r"\+359 2 \d{3} \d{4}|\+359-2-\d{3}-\d{4}\b"
result = re.findall(pattern, text)
print(", ".join(result))
