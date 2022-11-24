import re

text = input()
pattern = r"([\@\#])([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"
result = re.findall(pattern, text)
# x[1] is the second group which includes the first word and x[2] is the second word
all_pairs = [[x[1], x[2]] for x in result]
if len(all_pairs) == 0:
    print("No word pairs found!")
else:
    print(f"{len(all_pairs)} word pairs found!")
matched_strings = []
for string in all_pairs:
    if string[0] == string[1][::-1]:
        matched_strings.append(" <=> ".join(string))
if len(matched_strings) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(matched_strings))
