import re

text = input()
pattern = r"\s(([a-z0-9]+[a-z0-9\.\-\_]*)@[a-z\-]+(\.[a-z]+)+)\b"
result = re.findall(pattern, text)
for email in result:
    # index 0 represents group 1 which includes the whole match/email
    print(email[0])
