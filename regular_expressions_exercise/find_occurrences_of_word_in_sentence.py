import re

text = input()
word_to_search_for = input()
pattern = fr"\b({word_to_search_for})\b"
result = re.findall(pattern, text, re.I)
print(len(result))
