import re

number_of_strings = int(input())
pattern = r"^([\$%])([A-Z][a-z]{2,})\1: \[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$"
for _ in range(number_of_strings):
    string = input()
    result = re.search(pattern, string)
    if result:
        tag = result.group(2)
        letters = [int(x) for x in result.groups()[2:]]
        message = ""
        for i in letters:
            message += chr(i)
        print(f"{tag}: {message}")
    else:
        print("Valid message not found!")
